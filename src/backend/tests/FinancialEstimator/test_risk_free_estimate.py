import pytest
import numpy as np
from backend.HedgingEngine.FinancialEstimator.RiskFreeRateEstimator import RiskFreeRateEstimator

def test_mean_estimate():
    estimator = RiskFreeRateEstimator()

    # Cas normal
    rates = [0.01, 0.015, 0.02, 0.025, 0.03]
    expected_mean = np.mean(rates)
    assert estimator.mean_estimate(rates) == pytest.approx(expected_mean, rel=1e-6)

    # Cas avec un seul élément
    single_rate = [0.02]
    assert estimator.mean_estimate(single_rate) == pytest.approx(0.02, rel=1e-6)

    # Cas avec valeurs négatives
    negative_rates = [-0.01, 0.00, 0.01]
    expected_mean_negative = np.mean(negative_rates)
    assert estimator.mean_estimate(negative_rates) == pytest.approx(expected_mean_negative, rel=1e-6)

    # Cas avec liste vide (devrait lever une exception)
    with pytest.raises(ValueError):
        estimator.mean_estimate([])

