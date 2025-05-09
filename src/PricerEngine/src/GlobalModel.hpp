#ifndef Global_MODEL_HPP
#define Global_MODEL_HPP
#include "pnl/pnl_matvect.h"
#include "pnl/pnl_vector.h"
#include "pnl/pnl_matrix.h"
#include "pnl/pnl_random.h"
#include "RiskyAsset.hpp"
#include "Currency.hpp"
#include "TimeGrid.hpp"
#include <iostream>
#include <vector>
#include <map>
#include "InterestRateModel.hpp"
#include "pricing.pb.h"          // Pour les messages (PricingInput, etc.)
#include "pricing.grpc.pb.h" 



class GlobalModel
{
public:
    PnlMat *L;            /// raccine carrée de matrice de corrélation
    PnlVect *G;           /// Vector for simulation
    std::vector<std::unique_ptr<RiskyAsset>> assets ;
    std::vector<std::unique_ptr<Currency>>  currencies;
    
    InterestRateModel domesticInterestRate;
    TimeGrid monitoringTimeGrid;
    int model_size ;


public:
    GlobalModel();
    GlobalModel(const grpc_pricer::PricingInput& input);
    ~GlobalModel();

    Currency *getCurrencyById(std::string id);

    /**
     * Génère une trajectoire du modèle et la stocke dans path (simulation conditionnelle)
     *
     * @param[out] path contient une trajectoire du modèle.
     * C'est une matrice de taille (N+1) x D
     * @param[in] past : matrice de taille (i+1)*D avec i last-index
     * @param[in] t  :  temps actuel
     * @param[in] path : matrice de taille (N+1)xD
     * @param[in] rng : génerateur des nombres aléatoires
     */
    void asset(const PnlMat *past, double t, PnlMat *path, PnlRng *rng);

    /**
     * simuler 2 trajectoires utilisant les mêmes aléas Browniens mais shiftées l’une par rapport à l’autre
     *
     * @param[in] d : index of colonne
     * @param[in] h : double
     * @param[in] path : matrice de taille (N + 1)*D qui contient la simulation du modéle
     * @param[in] t : current time 
     *
     */
    void shift_asset(int d, double t, double h, PnlMat *path);
};
#endif