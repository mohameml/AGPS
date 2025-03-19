import pytest
import numpy as np
from backend.HedgingEngine.FinancialEstimator.VolatilityEstimator import VolatilityEstimator

def test_volatility_estimation():
    prices = [100, 102, 101, 103, 105, 104]
    estimator = VolatilityEstimator()
    
    log_returns = np.log(np.array(prices[1:]) / np.array(prices[:-1]))
    expected_volatility_daily = np.std(log_returns)
    expected_volatility_annualized = expected_volatility_daily * np.sqrt(252)
    
    # Test avec annualisation
    assert pytest.approx(estimator.estimate_volatility(prices, annualize=True), rel=1e-6) == expected_volatility_annualized
    
    # Test sans annualisation
    assert pytest.approx(estimator.estimate_volatility(prices, annualize=False), rel=1e-6) == expected_volatility_daily
    print('Test passed')

def test_volatility_constant_prices():
    prices = [100, 100, 100, 100, 100]
    estimator = VolatilityEstimator()
    
    assert estimator.estimate_volatility(prices) == 0.0

def test_volatility_minimum_prices():
    prices = [100, 101]  # Seulement deux prix
    estimator = VolatilityEstimator()
    
    assert estimator.estimate_volatility(prices) == 0.0

test_volatility_estimation()