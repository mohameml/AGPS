#include "RiskyDynamics.hpp"
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"
#include <iostream>
#include <cmath>

RiskyDynamics::RiskyDynamics()
{
}

RiskyDynamics::RiskyDynamics(double drift, double realVolatility, PnlVect* volatilityVector_, int index)
    : drift(drift), realVolatility(realVolatility), index(index) {
    // Cloner volatilityVector_
    int len = volatilityVector_->size;
    this->volatilityVector = pnl_vect_create_from_double(len, 0.0);
    for (size_t i = 0; i < len; i++) {
        LET(this->volatilityVector, i) = GET(volatilityVector_, i);
    }
}


RiskyDynamics::~RiskyDynamics()
{
    if(volatilityVector)
        pnl_vect_free(&volatilityVector);
}



void RiskyDynamics::sampleNextDate(PnlMat *path, double step, const PnlVect *G, int index_time) {
    // Calculer la valeur de mise à jour
    double value = exp((drift - realVolatility * realVolatility / 2.0) * step + sqrt(step) * pnl_vect_scalar_prod(volatilityVector, G));

    // Mettre à jour la ligne suivante
    double s_t_d = MGET(path, index_time - 1, index);
    MLET(path, index_time, index) = s_t_d * value;
}


void RiskyDynamics::sampleNextDate(PnlMat *path, double step, const PnlVect *G, int index_time, bool isMonitoringDate) {

    // Calculer la valeur de mise à jour
    double value = exp((drift - realVolatility * realVolatility / 2.0) * step + sqrt(step) * pnl_vect_scalar_prod(volatilityVector, G));
    
    
    // Mettre à jour path en fonction de isMonitoringDate
    if (isMonitoringDate) {
        double s_t_d = MGET(path, index_time - 1, index);

        MLET(path, index_time, index) = s_t_d * value;
    } else {
        double s_t_d = MGET(path, index_time, index);
        MLET(path, index_time, index) = s_t_d * value;
    }
}