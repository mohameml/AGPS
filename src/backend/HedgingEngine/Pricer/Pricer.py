from abc import ABC, abstractmethod
from backend.HedgingEngine.Pricer.PricingParams import PricingParams
from backend.HedgingEngine.Pricer.PricingResults import PricingResults
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams


class Pricer(ABC):

    def __init__(self, financial_parameters: FinancialParams):
        self.params : FinancialParams = financial_parameters

    @abstractmethod
    def price_and_deltas(self, pricing_params: PricingParams) -> PricingResults :
        pass
