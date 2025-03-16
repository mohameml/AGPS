#include "Option.hpp"
#include <iostream>
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"
#include <vector>
#include <cmath>
#include "pricing.pb.h"


using namespace std;


Option::Option(const grpc_pricer::PricingInput& input)
{

    
    std::string domesticCurrencyId = input.domesticcurrencyid();

    double domesticRate = 0.0; // Taux d'intérêt de la devise domestique
    bool domesticCurrencyFound = false;

    for (const auto& currency : input.currencies()) {
        if (currency.id() == domesticCurrencyId) {
            domesticRate = currency.interestrate();
            break;
        }
    }


    this->domesticInterestRate = InterestRateModel(domesticRate, domesticCurrencyId);

    this->monitoringTimeGrid = TimeGrid(std::vector<double>(input.time_grid().begin(), input.time_grid().end()));
    this->maturity = monitoringTimeGrid.grid_time.back();

    
}

Option::~Option()
{
}

double barriere_plus_ou_moins_15(PnlVect* x){
    
    double max_perf = pnl_vect_max(x);

    if (max_perf > 0.15){
        return 0.15;
    } else if ( max_perf < -0.15){
        return -0.15;
    } else {
        return max_perf;
    }

}


void Option::computeDividends(const PnlMat* matrix,  PnlVect* perfDiv){


    PnlVect *row_i = pnl_vect_create(5);
    PnlVect *row_i_1 = pnl_vect_create(5);

    for (int i = 1; i<5; i++){

        pnl_mat_get_row(row_i, matrix, i);
        pnl_mat_get_row(row_i_1, matrix, i-1);

        pnl_vect_minus_vect(row_i, row_i_1); 
        pnl_vect_div_vect_term(row_i, row_i_1); 

        double perf_i = std::max(pnl_vect_min(row_i), 0.0);
        pnl_vect_set(perfDiv, i-1, perf_i);
    }
    pnl_vect_free(&row_i);
    pnl_vect_free(&row_i_1);

}





void perf(const PnlMat* matrix, PnlVect* perf) {
    PnlVect *row_i = pnl_vect_create(5);
    PnlVect *row_0 = pnl_vect_create(5); 

    std::vector<int> excluded_indices;

    pnl_mat_get_row(row_0, matrix, 0);

    for (int i = 1; i < 6; i++) { 
        pnl_mat_get_row(row_i, matrix, i);

        // Calcul de la performance relative
        pnl_vect_minus_vect(row_i, row_0);
        pnl_vect_div_vect_term(row_i, row_0);

        // Exclure les indices déjà sélectionnés
        for (int j = 0; j < excluded_indices.size(); j++) {
            int idx = excluded_indices[j];
            if (idx != -1) {  // Si l'indice est valide (pas déjà exclu)
                LET(row_i, idx) = -INFINITY;
            }
        }

        // Calcul de la performance pour cette ligne
        double perf_i = barriere_plus_ou_moins_15(row_i);

        // Trouver l'indice de la meilleure performance
        double max_value;
        int max_index;
        pnl_vect_max_index(&max_value, &max_index, row_i);

        // Ajouter l'indice exclu à la liste des indices exclus, si nécessaire
        bool already_excluded = false;
        for (int j = 0; j < excluded_indices.size(); j++) {
            if (excluded_indices[j] == max_index) {
                already_excluded = true;
                break;
            }
        }

        if (!already_excluded) {
            // Ajouter l'indice à excluded_indices
            excluded_indices.push_back(max_index);
        }

        pnl_vect_set(perf, i-1, perf_i);
    }

    pnl_vect_free(&row_i);
    pnl_vect_free(&row_0);
}




double barriere_800_euros(double x){

    if (x < 800){
        return 800;
    }else{
        return x;
    }
}


double Option::payOff(const PnlMat* path){
    
    PnlMat *matrix = pnl_mat_create(path->m, 5);  // Même nombre de lignes, 5 colonnes
    // Extraction des colonnes 0 à 4 (5 colonnes des indices)
    pnl_mat_extract_subblock(matrix, path, 0, 0, path->m, 5);


    double perfValue = 0.0;
    PnlVect *perfDiv = pnl_vect_create(4);
    PnlVect *perfFlux = pnl_vect_create(5);
    computeDividends(matrix, perfDiv);
    perf(matrix, perfFlux);

    double res = 0.0;

    for (int i=1; i < 5; i++){

        double t_i = monitoringTimeGrid.at(i);
        double t_f = monitoringTimeGrid.at(5);
        perfValue += pnl_vect_get(perfFlux, i-1);
        res += pnl_vect_get(perfDiv, i-1)*100 *domesticInterestRate.account(t_i, t_f);

        std::cout << "Dividence numéro : " << i-1 << std::endl;
        std::cout << "Valeur : " << pnl_vect_get(perfDiv, i-1)*100 *domesticInterestRate.account(t_i, t_f) << std::endl;

    }

    perfValue += pnl_vect_get(perfFlux, 4);
    double flux_Tc = barriere_800_euros(1000*(1+0.60*perfValue));
    
    std::cout << "Flux à la date Tc : " << flux_Tc << std::endl;

    res += flux_Tc;
    pnl_mat_free(&matrix);
    return res;
}