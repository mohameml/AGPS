#ifndef OPTION_HPP
#define OPTION_HPP

#include <iostream>
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"
#include "json_reader.hpp"
#include "InterestRateModel.hpp"
#include <vector> 
#include "TimeGrid.hpp"




class Option
{
public:

    InterestRateModel domesticInterestRate;
    TimeGrid monitoringTimeGrid;

public:
    Option();
    /**
     * Constructeur de parsing :
     */
    Option(InterestRateModel domesticInterestRate, TimeGrid monitoringTimeGrid);

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

    virtual double computeDividends(double t, const PnlMat* matrix);
    virtual double payOff(const PnlMat *matrix) = 0;
};


#endif



