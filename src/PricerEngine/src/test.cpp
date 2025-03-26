#include "GlobalModel.hpp"
#include "Option.hpp"
#include "MonteCarlo.hpp"
#include "pnl/pnl_random.h"
#include "pnl/pnl_matrix.h"
#include <iostream>

// Fonction pour créer un objet PricingInput avec les données fournies
grpc_pricer::PricingInput createTestInput() {
    grpc_pricer::PricingInput input;

    // Remplir past (historique des prix)
    grpc_pricer::PastLines* pastLine = input.add_past();
    pastLine->add_value(2375.34);
    pastLine->add_value(661.63009877101706);
    pastLine->add_value(4772.3827746362058);
    pastLine->add_value(6.4443441373674064);
    pastLine->add_value(2075.9374500490085);
    pastLine->add_value(0.75397722988765736);
    pastLine->add_value(1.1247078338234184);
    pastLine->add_value(0.0076097822959997714);
    pastLine->add_value(0.550704968709945);

    // Remplir monitoringDateReached
    input.set_monitoringdatereached(true);

    // Remplir time
    input.set_time(0.0);

    // Remplir currencies
    grpc_pricer::Currency* eur = input.add_currencies();
    eur->set_id("EUR");
    eur->set_interestrate(0.0069618778280542987);

    grpc_pricer::Currency* usd = input.add_currencies();
    usd->set_id("USD");
    usd->set_interestrate(0.0041069758672699847);
    usd->set_volatility(0.096598910043132771);

    grpc_pricer::Currency* gbp = input.add_currencies();
    gbp->set_id("GBP");
    gbp->set_interestrate(0.0073841251885369526);
    gbp->set_volatility(0.078170184826813149);

    grpc_pricer::Currency* jpy = input.add_currencies();
    jpy->set_id("JPY");
    jpy->set_interestrate(0.0024464177978883862);
    jpy->set_volatility(0.12881009473359448);

    grpc_pricer::Currency* aud = input.add_currencies();
    aud->set_id("AUD");
    aud->set_interestrate(0.039447699849170438);
    aud->set_volatility(0.10026207344543647);

    // Remplir domesticCurrencyId
    input.set_domesticcurrencyid("EUR");

    // Remplir assets
    grpc_pricer::Asset* asset1 = input.add_assets();
    asset1->set_currencyid("EUR");
    asset1->set_volatility(0.23121705813542);

    grpc_pricer::Asset* asset2 = input.add_assets();
    asset2->set_currencyid("USD");
    asset2->set_volatility(0.17758056635452812);

    grpc_pricer::Asset* asset3 = input.add_assets();
    asset3->set_currencyid("GBP");
    asset3->set_volatility(0.16904759292955523);

    grpc_pricer::Asset* asset4 = input.add_assets();
    asset4->set_currencyid("JPY");
    asset4->set_volatility(0.21037732628424263);

    grpc_pricer::Asset* asset5 = input.add_assets();
    asset5->set_currencyid("AUD");
    asset5->set_volatility(0.16495413502313466);

    // Remplir correlations
    std::vector<std::vector<double>> correlation_values = {
        {1, 0.718684, 0.882601, 0.236849, 0.342541, 0.063826, 0.044087, 0.040928, 0.040303},
        {0.718684, 1, 0.714898, 0.152891, 0.249545, 0.039842, 0.015353, 0.017566, 0.027206},
        {0.882601, 0.714898, 1, 0.269744, 0.408338, 0.052873, 0.030251, 0.038242, 0.021726},
        {0.236849, 0.152891, 0.269744, 1, 0.582785, -0.002399, 0.036767, -0.024029, 0.009065},
        {0.342541, 0.249545, 0.408338, 0.582785, 1, 0.022352, 0.043058, 0.002039, -0.002607},
        {0.063826, 0.039842, 0.052873, -0.002399, 0.022352, 1, 0.548554, 0.648919, 0.198864},
        {0.044087, 0.015353, 0.030251, 0.036767, 0.043058, 0.548554, 1, 0.382081, 0.332128},
        {0.040928, 0.017566, 0.038242, -0.024029, 0.002039, 0.648919, 0.382081, 1, 0.056605},
        {0.040303, 0.027206, 0.021726, 0.009065, -0.002607, 0.198864, 0.332128, 0.056605, 1}
    };

    for (const auto& row : correlation_values) {
        grpc_pricer::CorrelationMatrix* correlation = input.add_correlations();
        for (double value : row) {
            correlation->add_values(value);
        }
    }

    // Remplir time_grid
    std::vector<double> time_grid = {0, 0.94841269841269837, 1.9841269841269842, 3.0198412698412698, 4.0515873015873014, 5.2619047619047619};
    for (double t : time_grid) {
        input.add_time_grid(t);
    }

    return input;
}

int testGlobalModel() {
    // Créer un objet PricingInput de test
    grpc_pricer::PricingInput input = createTestInput();
    // Tester le constructeur de GlobalModel
    GlobalModel model(input);


    // Tester la méthode asset
    int N = model.monitoringTimeGrid.len();
    PnlMat* past = pnl_mat_create_from_scalar(3, 9, 100.0); // Matrice 3x2 remplie de 100.0
    PnlMat* path = pnl_mat_create(N, 9); // Matrice 5x2 pour stocker le chemin simulé
    PnlRng* rng = pnl_rng_create(PNL_RNG_MERSENNE);
    pnl_rng_sseed(rng, 42); // Initialiser le générateur de nombres aléatoires

    double t = 2.5; // Temps actuel
    model.asset(past, t, path, rng);

    // Afficher le chemin simulé
    std::cout << "Simulated path:" << std::endl;
    pnl_mat_print(path);

    // Libérer la mémoire
    pnl_mat_free(&past);
    pnl_mat_free(&path);
    pnl_rng_free(&rng);

    return 0;
}







int testPayoff() {

    grpc_pricer::PricingInput input = createTestInput();
    Option option(input);

    PnlMat *test_matrix = pnl_mat_create(6, 9);

    double data[6][9] = {
        {2553.41,  927.45,  4579.64,  875.91,  3687,    0, 0, 0, 0},
        {3017.8,   1132.99, 5500.34,  915.75,  4876.3,  0, 0, 0, 0},
        {2844.17,  1270.2,  6013.87,  911.8,   4742.5,  0, 0, 0, 0},
        {2349.89,  1277.3,  5668.45,  742.99,  4187.8,  0, 0, 0, 0},
        {2709.35,  1466.47, 6089.84,  888.51,  4723.8,  0, 0, 0, 0},
        {3069.16,  1826.77, 6730.73,  1292.15,  5324.9,  0, 0, 0, 0}
    };
    
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 9; j++) {
            MLET(test_matrix, i, j) = data[i][j];
        }
    }
    

    double payoff = option.payOff(test_matrix);
    std::cout << "Payoff: " << payoff << std::endl;

    pnl_mat_free(&test_matrix);


    return 0;
}

PnlMat* convertPastToPnlMat(const grpc_pricer::PricingInput& input) {
    // Find size
    int m, n;
    m = input.past_size();
    if (m == 0) {
        return NULL;
    }
    n = input.past(0).value_size();
    for (int i = 0; i < input.past_size(); i++) {
        const grpc_pricer::PastLines &pastLine = input.past(i);
        if (pastLine.value_size() != n) {
            std::cerr << "size mismatch in past" << std::endl;
            return NULL;
        }
    }
    // Parse data
    PnlMat *past = pnl_mat_create(m, n);
    for (int i = 0; i < input.past_size(); i++) {
        const grpc_pricer::PastLines &pastLine = input.past(i);
        for (int j = 0; j < pastLine.value_size(); j++) {
            MLET(past, i, j) = pastLine.value(j);
        }
    }
    return past;
}


int testMontCarlo() {
    // Créer un objet PricingInput de test
    grpc_pricer::PricingInput input = createTestInput();
    // Tester le constructeur de GlobalModel
    double price, priceStdDev;
    PnlVect *delta = pnl_vect_create_from_scalar(input.correlations_size(),0.); // Initialiser avec une taille appropriée
    PnlVect *deltaStdDev = pnl_vect_create_from_scalar(input.correlations_size(),0.); // Initialiser avec une taille appropriée
    
    bool isMonitoringDate = input.monitoringdatereached();
    double currentDate = input.time();
    PnlMat *past = convertPastToPnlMat(input); 

    MonteCarlo* Pricer = new MonteCarlo(input);

    if (past == NULL) {
        return -1;
    }

    // std::cout << "========== t = " << input.time() << "===========" << std::endl;
    // pnl_mat_print(past);

    Pricer->priceAndDelta(currentDate, past, price, priceStdDev, delta, deltaStdDev);

    std::cout << "price = " << price << std::endl;
    std::cout << "priceStdDev = " << priceStdDev << std::endl;
    std::cout << "Deltas = ";
    pnl_vect_print_asrow(delta);
    std::cout << "DeltasStdDev  = ";
    pnl_vect_print_asrow(deltaStdDev);


    pnl_mat_free(&past);
    pnl_vect_free(&delta);
    pnl_vect_free(&deltaStdDev);
    delete Pricer;

    return 0;
}





int main() {
    // testGlobalModel();
    testPayoff();
    // testMontCarlo();
    return 0;
}
