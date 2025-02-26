#include "Option.hpp"
#include <iostream>
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"

using namespace std;

Option::Option()
{
}

Option::Option(InterestRateModel domesticInterestRate, TimeGrid monitoringTimeGrid)
{

    this->domesticInterestRate = domesticInterestRate;
    this->monitoringTimeGrid = monitoringTimeGrid;
    
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

        std::cout << "Dividendes rows  : " << std::endl;
        pnl_vect_print_nsp(row_i);
        double perf_i = std::max(pnl_vect_min(row_i), 0.0);
        pnl_vect_set(perfDiv, i-1, perf_i);
    }

    pnl_vect_free(&row_i);
    pnl_vect_free(&row_i_1);

}


void perf(const PnlMat* matrix, PnlVect* perf){

    PnlVect *row_i = pnl_vect_create(5);
    PnlVect *row_0 = pnl_vect_create(5);
    PnlVectInt *excluded_indices = pnl_vect_int_create(5);


    for (int i = 1; i < 6; i++){

        pnl_mat_get_row(row_i, matrix, i);

        pnl_vect_minus_vect(row_i, row_0); 
        pnl_vect_div_vect_term(row_i, row_0); 

        // Exclure les indices déjà sélectionnés
        for (int j = 0; j < excluded_indices->size; j++) {
            int idx = GET_INT(excluded_indices, j);
            LET(row_i, idx) = -INFINITY; 
        }
        
        std::cout << "Performance rows  : " << std::endl;
        pnl_vect_print_nsp(row_i);

        double perf_i = barriere_plus_ou_moins_15(row_i);

        // Trouver l'indice du max et l'ajouter aux exclus
        double max_value;
        int max_index;
        pnl_vect_max_index(&max_value, &max_index, row_i);

        pnl_vect_int_set(excluded_indices, i-1, max_index);

        pnl_vect_set(perf, i-1, perf_i);
    }

    pnl_vect_free(&row_i);
    pnl_vect_free(&row_0);
    pnl_vect_int_free(&excluded_indices);
}




double barriere_800_euros(double x){

    if (x < 800){
        return 800;
    }else{
        return x;
    }
}


double Option::payOff(const PnlMat* matrix){
    
    double perfValue = 0.0;
    PnlVect *perfDiv = pnl_vect_create(4);
    PnlVect *perfFlux = pnl_vect_create(5);
    computeDividends(matrix, perfDiv);
    perf(matrix, perfFlux);

    double res = 0.0;

    for (int i=1; i < 5; i++){

        //double t_i = monitoringTimeGrid.at(i);
        //double t_f = monitoringTimeGrid.at(5);
        perfValue += pnl_vect_get(perfFlux, i-1);
        std::cout << "Performance : " << pnl_vect_get(perfFlux, i-1) << std::endl;

        res += pnl_vect_get(perfDiv, i-1)*100;  //*domesticInterestRate.account(t_i, t_f);

        std::cout << "Dividende : " << pnl_vect_get(perfDiv, i-1)*100 << std::endl;
    }

    perfValue += pnl_vect_get(perfFlux, 4);
    double flux_Tc = barriere_800_euros(1000*(1+perfValue));
    
    std::cout << "Flux à la date Tc : " << flux_Tc << std::endl;

    res += flux_Tc;
    return res;
}