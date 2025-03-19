#include "GlobalModel.hpp"
#include "pricing.pb.h"



GlobalModel::GlobalModel()
{
}

GlobalModel::~GlobalModel()
{
    pnl_vect_free(&G);
    pnl_mat_free(&L);
}

GlobalModel::GlobalModel(const grpc_pricer::PricingInput& input)
{
    // ====== monitoringTimeGrid === 
    monitoringTimeGrid = TimeGrid(std::vector<double>(input.time_grid().begin(), input.time_grid().end()));
    
    // ==== Correlations and matrice cholesky :  ==== 
    L = pnl_mat_create(input.correlations().size(), input.correlations().size());
    for (size_t i = 0; i < input.correlations().size(); i++) {
        for (size_t j = 0; j < input.correlations(i).values().size(); j++) {
            MLET(L, i, j) = input.correlations(i).values(j);
        }
    }
    pnl_mat_chol(L);
    
    model_size = L->n;
    
    // ===== vecteur of simulation G : ===== 
    G = pnl_vect_create_from_double(model_size, 0.0);
    
    // ================== Currencies ============== 
    PnlVect* volatilityVector = pnl_vect_create_from_double(model_size, 0.0);
    
    // Accéder à domesticCurrencyId via la méthode getter
    std::string domesticCurrencyId = input.domesticcurrencyid();
    int index = 0;
    int assetNb = model_size - (input.currencies().size() - 1);
    
    // Parcourir les currencies avec la méthode getter
    for (const auto& currency : input.currencies()) {
        std::string currencyId = currency.id();
        double rf = currency.interestrate();
        double realVolatility = currency.volatility();

        if (currencyId == domesticCurrencyId) {
            this->domesticInterestRate = InterestRateModel(rf, currencyId);
        } else {
            pnl_mat_get_row(volatilityVector, L, assetNb + index);
            pnl_vect_mult_scalar(volatilityVector, realVolatility);

            currencies.push_back(std::make_unique<Currency>(
                domesticInterestRate,
                InterestRateModel(rf, currencyId),
                realVolatility,
                volatilityVector,
                assetNb + index
            ));
            index++;
        }
    }
    
    // ================== Assets ============== 
    int index_asset = 0;
    
    // Parcourir les assets avec la méthode getter
    for (const auto& asset : input.assets()) {
        std::string currencyId = asset.currencyid();
        double realVolatility = asset.volatility();
        
        if (currencyId == domesticCurrencyId) {
            pnl_mat_get_row(volatilityVector, L, index_asset);
            pnl_vect_mult_scalar(volatilityVector, realVolatility);
            assets.push_back(std::make_unique<RiskyAsset>(
                domesticInterestRate,
                realVolatility,
                volatilityVector,
                index_asset
            ));
        } else {
            Currency* currencyOfAsset = getCurrencyById(currencyId);
            pnl_mat_get_row(volatilityVector, L, index_asset);
            pnl_vect_mult_scalar(volatilityVector, realVolatility);
            pnl_vect_plus_vect(volatilityVector, currencyOfAsset->volatilityVector);
            double real_vol = pnl_vect_norm_two(volatilityVector);
            assets.push_back(std::make_unique<RiskyAsset>(
                domesticInterestRate,
                real_vol,
                volatilityVector,
                index_asset
            ));
        }
        index_asset++;
    }
    
    pnl_vect_free(&volatilityVector);
}



Currency* GlobalModel::getCurrencyById(std::string id) {
    for (const auto& curr : currencies)
    {
        if(curr->foreignInterestRate.id == id) {
            return curr.get();
        }
    }
    
    return nullptr;
    
}

void GlobalModel::asset(const PnlMat *past, double t, PnlMat *path, PnlRng *rng) {

    int last_index = monitoringTimeGrid.getLastIndex(t);

    if (last_index == monitoringTimeGrid.len() - 1) {

        pnl_mat_extract_subblock(path, past, 0, past->m, 0, past->n);
        return;
    }

    pnl_mat_set_subblock(path, past, 0, 0);
    pnl_vect_rng_normal(G, model_size, rng);
    double step = (monitoringTimeGrid.at(last_index + 1) - t);
    bool isMonitoringDate = monitoringTimeGrid.has(t);


    for (const auto& risky_asset : assets) {
        risky_asset->sampleNextDate(path, step, G, last_index + 1, isMonitoringDate);
    }
    std::cout << "je rentre dans currency" << std::endl;

    for (const auto& currency : currencies) {
        currency->sampleNextDate(path, step, G, last_index + 1, isMonitoringDate);
    }

    for (size_t i = last_index + 2; i < monitoringTimeGrid.len(); i++) {

        step = (monitoringTimeGrid.at(i) - monitoringTimeGrid.at(i - 1));
        pnl_vect_rng_normal(G, model_size, rng);
        pnl_vect_print(G);

        for (const auto& risky_asset : assets) {
            risky_asset->sampleNextDate(path, step, G, i);
        }

        for (const auto& currency : currencies) {
            currency->sampleNextDate(path, step, G, i);
        }
    }
}


void GlobalModel::shift_asset(int d, double t, double h, PnlMat *path)
{
    
    int last_index;
    
    if(monitoringTimeGrid.has(t)) {
        last_index = monitoringTimeGrid.getLastIndex(t);
    } else {
        last_index = monitoringTimeGrid.getLastIndex(t) + 1 ;
    }
    
    
    for (int i = last_index ; i < path->m; i++)
    {
        MLET(path, i, d) *= h;
    };
}
