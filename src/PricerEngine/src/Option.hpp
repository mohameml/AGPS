#ifndef OPTION_HPP
#define OPTION_HPP

#include <iostream>
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"
#include "InterestRateModel.hpp"
#include "TimeGrid.hpp"
#include "pricing.pb.h"          // Pour les messages (PricingInput, etc.)
#include "pricing.grpc.pb.h" 





class Option
{
public:

    InterestRateModel domesticInterestRate;
    TimeGrid monitoringTimeGrid;
    double maturity;
    PnlMat* matrix;;

public:
    Option();
    /**
     * Constructeur de parsing :
     */
    Option(const grpc_pricer::PricingInput& input);
    //Option(InterestRateModel domesticInterestRate, TimeGrid monitoringTimeGrid);

    /**
     * Destructeur
     */
    ~Option();

    /**
     * Calcule la valeur du payoff
     *
     * @param[in] matrix est une matrice  de taille (dates + 1)*size
     *  ligne d'index i de la matrice continet la valeur de l'actif du sous-jacent à t = t_i
     */

    void computeDividends(const PnlMat* matrix, PnlVect* perfDiv);
    double payOff(const PnlMat *matrix);
};


#endif



