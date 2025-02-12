from abc import ABC, abstractmethod

from backend.HedgingEngine.Pricer.PricingParams import PricingParams
from backend.HedgingEngine.Pricer.PricingResults import PricingResults


class TestParameters:
    # Définir les propriétés de TestParameters ici
    pass


class Pricer(ABC):
    
    def __init__(self, test_parameters: TestParameters):
        self.params = test_parameters

    @abstractmethod
    def price_and_deltas(self, pricing_params: PricingParams) -> PricingResults:
        pass
