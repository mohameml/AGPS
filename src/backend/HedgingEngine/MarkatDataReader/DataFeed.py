from datetime import datetime
from typing import Dict
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.IndexPrice import IndexPrice
from backend.HedgingEngine.MarkatDataReader.ExchangeRate import ExchangeRate
from backend.HedgingEngine.MarkatDataReader.InterestRate import InterestRate



class DataFeed :
    def __init__(
        self, date: datetime, 
        dict_index_price: Dict[EnumIndex, IndexPrice], 
        dict_interest_rate: Dict[EnumCurrency, InterestRate], 
        dict_exchange_rate: Dict[EnumCurrency, ExchangeRate]
    ):
        self.date = date
        self.dict_index_price = dict_index_price
        self.dict_interest_rate = dict_interest_rate
        self.dict_exchange_rate = dict_exchange_rate

    def display_info(self):
        print(f"=========== t = {self.date} =========")
        for key in self.dict_index_price.keys() :
            print(f'\t the price of index {key.value} is : {self.dict_index_price[key].price} ')

        for key in self.dict_interest_rate.keys() :
            print(f'\t the intersat rate of  {key.value} is : {self.dict_interest_rate[key].rate} ')
        
        for key in self.dict_exchange_rate.keys() :
            print(f'\t the exchange rate  of  {key.value} to EUR is : {self.dict_exchange_rate[key].rate} ')




