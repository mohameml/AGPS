import pytest
import numpy as np
from backend.HedgingEngine.FinancialEstimator.CorrelationMatrixEstimator import CorrelationMatrixEstimator

def test_estimate_correlation_matrix_shape():
    estimator = CorrelationMatrixEstimator()

    list_prices = np.array([
        [100, 102, 101, 105, 110],  # Actif 1
        [50, 52, 51, 55, 60],       # Actif 2
        [200, 198, 202, 207, 210]   # Actif 3
    ])

    correlation_matrix = estimator.estimate_correlation_matrix(list_prices)

    # Vérifier la forme de la matrice (doit être carrée)
    assert correlation_matrix.shape == (3, 3)

def test_correlation_matrix_diagonal():
    estimator = CorrelationMatrixEstimator()

    list_prices = np.array([
        [100, 102, 101, 105, 110],  # Actif 1
        [50, 52, 51, 55, 60],       # Actif 2
        [200, 198, 202, 207, 210]   # Actif 3
    ])

    correlation_matrix = estimator.estimate_correlation_matrix(list_prices)

    # Vérifier que la diagonale est bien égale à 1 (corrélation d'un actif avec lui-même)
    assert np.allclose(np.diag(correlation_matrix), np.ones(3))

def test_high_correlation():
    estimator = CorrelationMatrixEstimator()

    list_prices_high_corr = np.array([
        [100, 101, 102, 103, 104],  # Actif 1
        [200, 202, 204, 206, 208]   # Actif 2 (double du premier, donc corrélation proche de 1)
    ])

    correlation_matrix_high_corr = estimator.estimate_correlation_matrix(list_prices_high_corr)

    assert correlation_matrix_high_corr[0, 1] > 0.99  # Corrélation proche de 1
    assert correlation_matrix_high_corr[1, 0] > 0.99

def test_random_correlation():
    estimator = CorrelationMatrixEstimator()

    # Cas avec actifs non corrélés (rendements aléatoires)
    np.random.seed(42)
    random_prices = np.random.rand(3, 10) * 100
    correlation_matrix_random = estimator.estimate_correlation_matrix(random_prices)

    # Vérifier que les corrélations ne sont pas toutes 1 (cas idéalement proche de 0)
    assert not np.allclose(correlation_matrix_random, np.eye(3))

def test_single_asset():
    estimator = CorrelationMatrixEstimator()

    # Cas avec un seul actif (doit retourner une matrice 1x1 avec valeur 1)
    single_asset_prices = np.array([[100, 102, 104, 106, 108]])
    correlation_matrix_single = estimator.estimate_correlation_matrix(single_asset_prices)

    assert correlation_matrix_single.shape == (1, 1)
    assert correlation_matrix_single[0, 0] == 1.0

def test_constant_prices():
    estimator = CorrelationMatrixEstimator()

    # Cas avec des actifs ayant des prix constants (devrait lever une erreur)
    constant_prices = np.array([
        [100, 100, 100, 100, 100],
        [50, 50, 50, 51, 50]
    ])
    
    # np.corrcoef peut renvoyer NaN si variance nulle
    with pytest.raises(ValueError):  
        estimator.estimate_correlation_matrix(constant_prices)

