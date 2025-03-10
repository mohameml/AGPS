import unittest
import numpy as np
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator

class TestFinancialEstimator(unittest.TestCase):

    def setUp(self):
        self.financial_estimator = FinancialEstimator()

    def test_estimate_correlation_matrix(self):
        list_prices = [
            [100, 101, 102, 103, 104],
            [200, 202, 204, 206, 208],
            [300, 303, 306, 309, 312]
        ]
        expected_shape = (3, 3)
        correlation_matrix = self.financial_estimator.corrMatrixEstimator.estimate_correlation_matrix(np.array(list_prices))
        self.assertEqual(correlation_matrix.shape, expected_shape)
        self.assertTrue(np.allclose(correlation_matrix, correlation_matrix.T, atol=1e-8))  # Check if the matrix is symmetric

    def test_estimate_volatility(self):
        list_price = [100, 101, 102, 103, 104]
        volatility = self.financial_estimator.volatilityEstimator.estimate_volatility(list_price)
        self.assertIsInstance(volatility, float)
        self.assertGreater(volatility, 0)

    def test_mean_estimate(self):
        r_t = [0.01, 0.02, 0.015, 0.017, 0.016]
        mean_rate = self.financial_estimator.riskFreeEstimator.mean_estimate(r_t)
        self.assertIsInstance(mean_rate, float)
        self.assertAlmostEqual(mean_rate, np.mean(r_t))

if __name__ == '__main__':
    unittest.main()
