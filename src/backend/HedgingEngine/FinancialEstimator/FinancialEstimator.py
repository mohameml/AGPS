from backend.HedgingEngine.FinancialEstimator.VolatilityEstimator import VolatilityEstimator
from backend.HedgingEngine.FinancialEstimator.CorrelationMatrixEstimator import CorrelationMatrixEstimator
from backend.HedgingEngine.FinancialEstimator.RiskFreeRateEstimator import RiskFreeRateEstimator


class FinancialEstimator :

    def __init__(self):
        self.volatilityEstimator : VolatilityEstimator = VolatilityEstimator()
        self.riskFreeEstimator : RiskFreeRateEstimator = RiskFreeRateEstimator()
        self.corrMatrixEstimator : CorrelationMatrixEstimator = CorrelationMatrixEstimator()
