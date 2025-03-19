#include "Currency.hpp"

Currency::Currency()
{
}

Currency::Currency(InterestRateModel domesticInterestRate, InterestRateModel foreignInterestRate, double volatility, PnlVect* volatilityVector, int index)
    : RiskyDynamics(domesticInterestRate.rate - foreignInterestRate.rate, volatility, volatilityVector, index),
      domesticInterestRate(domesticInterestRate),
      foreignInterestRate(foreignInterestRate) {}
// Currency::Currency(InterestRateModel domesticInterestRate, InterestRateModel foreignInterestRate, double volatility, PnlVect* volatilityVector , int index):RiskyDynamics(0.0 , volatility , volatilityVector , index)
// {
//     this->domesticInterestRate = domesticInterestRate;
//     this->foreignInterestRate = foreignInterestRate;
//     this->drift = domesticInterestRate.rate ;
// }




Currency::~Currency()
{
}

