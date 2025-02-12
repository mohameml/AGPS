#include "Option.hpp"
#include <iostream>

#include "CallCurrencyOption.hpp"
#include "CallQuantoOption.hpp"
#include "ForeignAsianOption.hpp"
#include "QuantoExchangeOption.hpp"
#include "ForeignPerfBasketOption.hpp"
#include <map>

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




double Option::computeDividends(const PnlMat* matrix, const PnlVect* perfDiv){


    PnlVect *row_i = pnl_vect_create(5);
    PnlVect *row_i_1 = pnl_vect_create(5);

    for (int i = 1; i<5; i++){

        pnl_mat_get_row(row_i, matrix, i);
        pnl_mat_get_row(row_i_1, matrix, i - 1);

        pnl_vect_minus(row_i, row_i_1); 
        pnl_vect_div_vect_term(row_i, row_i_1); 

        double perf_i = std::max(pnl_vect_min(row_i), 0);
        pnl_vect_set(perfDiv, i-1, perf_i);
    }

    pnl_vect_free(&row_i);
    pnl_vect_free(&row_i_1);

}


double Option::payOff(const PnlMat* matrix){

    return 0.0;
}