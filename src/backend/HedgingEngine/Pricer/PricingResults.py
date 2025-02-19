from typing import List, Dict
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex

class PricingResults:
    
    def __init__(self, deltas: List[float], price: float, deltas_std_dev: List[float], price_std_dev: float, ids: List[EnumIndex]):

        self.deltas: Dict[EnumIndex, float] = {}
        self.deltas_std_dev: Dict[EnumIndex, float] = {}
        self.price: float = price
        self.price_std_dev: float = price_std_dev

        for i in range(len(deltas)):
            self.deltas[ids[i]] = deltas[i]
            self.deltas_std_dev[ids[i]] = deltas_std_dev[i]
