#include "GlobalModel.hpp"
#include "pnl/pnl_random.h"
#include "pnl/pnl_matrix.h"
#include <iostream>

// Fonction pour créer un objet PricingInput de test
grpc_pricer::PricingInput createTestInput() {
    grpc_pricer::PricingInput input;

    // Remplir time_grid
    input.add_time_grid(0.0);
    input.add_time_grid(1.0);
    input.add_time_grid(1.5);
    input.add_time_grid(2.0);
    input.add_time_grid(6.0);

    // Remplir currencies
    grpc_pricer::Currency* currency1 = input.add_currencies();
    currency1->set_id("USD");
    currency1->set_interestrate(0.05);
    currency1->set_volatility(0.1);

    grpc_pricer::Currency* currency2 = input.add_currencies();
    currency2->set_id("EUR");
    currency2->set_interestrate(0.03);
    currency2->set_volatility(0.2);

    // Remplir assets
    grpc_pricer::Asset* asset1 = input.add_assets();
    asset1->set_currencyid("USD");
    asset1->set_volatility(0.15);

    grpc_pricer::Asset* asset2 = input.add_assets();
    asset2->set_currencyid("EUR");
    asset2->set_volatility(0.25);

    // Remplir correlations
    grpc_pricer::CorrelationMatrix* correlation1 = input.add_correlations();
    correlation1->add_values(1.0);
    correlation1->add_values(0.5);

    grpc_pricer::CorrelationMatrix* correlation2 = input.add_correlations();
    correlation2->add_values(0.5);
    correlation2->add_values(1.0);

    // Remplir domesticCurrencyId
    input.set_domesticcurrencyid("USD");

    return input;
}

int main() {
    // Créer un objet PricingInput de test
    grpc_pricer::PricingInput input = createTestInput();

    // Tester le constructeur de GlobalModel
    GlobalModel model(input);

    // Afficher des informations pour vérifier que le constructeur fonctionne
    std::cout << "Model size: " << model.model_size << std::endl;
    std::cout << "Domestic currency ID: " << model.domesticInterestRate.id << std::endl;

    // Tester la méthode asset
    PnlMat* past = pnl_mat_create_from_scalar(3, 2, 100.0); // Matrice 3x2 remplie de 100.0
    PnlMat* path = pnl_mat_create(5, 2); // Matrice 5x2 pour stocker le chemin simulé
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
