from typing import Dict
import math
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed

class Portfolio:

    def __init__(self, dict_init: Dict[str, float], data: DataFeed, value: float):
        
        self.compositions = dict_init
        self.cash = value - sum(dict_init[key] * data.spot_list[key] for key in dict_init)
        self.date = data.date

    def update_compo(self, compos: Dict[str, float], feed: DataFeed, value: float):
        
        self.compositions = compos
        self.cash = value - sum(compos[key] * feed.spot_list[key] for key in compos)
        self.date = feed.date

    def get_portfolio_value(self, feed: DataFeed, time: float, r: float) -> float:

        value = sum(self.compositions[key] * feed.spot_list[key] for key in self.compositions) + self.cash * math.exp(r * time)
        
        return value
