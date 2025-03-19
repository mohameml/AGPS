from typing import Dict
import math
# from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from  datetime import datetime

class Portfolio:

    def __init__(self, dict_init: Dict[str, float], spot_list: Dict[str , float] , date : datetime, price: float):
        
        self.compositions = dict_init
        self.cash = price - sum(dict_init[key] * spot_list[key] for key in dict_init)
        self.date = date
        self.value = price

    def set_parms(self , compos: Dict[str, float] , cash : float , date : datetime) :
        self.compositions = compos
        self.cash = cash
        self.date = date

    def update_compo(self, compos: Dict[str, float],spot_list: Dict[str , float] , date, time : float, r : float):
        self.value = self.get_portfolio_value(spot_list, time, r)
        self.compositions = compos
        self.cash = self.value - sum(compos[key] * spot_list[key] for key in compos)
        self.date = date

    def get_portfolio_value(self, spot_list: Dict[str , float], time: float, r: float) -> float:

        value = sum(self.compositions[key] * spot_list[key] for key in self.compositions) + self.cash * math.exp(r * time)
        
        return value

    def display(self):
        print("compositions : ", self.compositions)
        print("cash : ", self.cash)
        print("date : ", self.date)