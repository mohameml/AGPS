from datetime import datetime
from typing import Dict
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.IndexPrice import IndexPrice
from backend.HedgingEngine.MarkatDataReader.ExchangeRate import ExchangeRate
from backend.HedgingEngine.MarkatDataReader.InterestRate import InterestRate
import numpy as np 
from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter
from backend.HedgingEngine.MarkatDataReader.EnumIndex import index_to_currency


class DataFeed :


    # TODO : fixe dict_interest_rate et MathDateConverter 
    def __init__(
        self, 
        date: datetime, 
        dict_index_price: Dict[EnumIndex, IndexPrice], 
        dict_exchange_rate: Dict[EnumCurrency, ExchangeRate],
        dict_interest_rate: Dict[EnumCurrency , InterestRate] ,
        T0 : datetime
    ):
        self.date = date

        # TODO : fixe nombreOfDaysWorksInOneYear : 

        mathDataConverter = MathDateConverter(252)
        self.t = mathDataConverter.ConvertToMathDistance(T0 , date) ,
        
        self.dict_index_price = dict_index_price
        self.dict_interest_rate = dict_interest_rate
        self.dict_exchange_rate = dict_exchange_rate
        self.nbAsset = len(self.dict_index_price) + len(self.dict_exchange_rate)



    def toDomesticMarket(self):
        res = []

        for index_name in EnumIndex :

            if index_to_currency[index_name] == EnumCurrency.EUR :
                res.append(self.dict_index_price[index_name].price) # S0_t0
            else : 
                index_price = self.dict_index_price[index_name]
                print(f'price for {index_name.value} = {index_price.price}')
                print(f'exchange rate  for {index_name.value} = {self.dict_exchange_rate[index_price.currency].rate }')
                price_in_domestic  = index_price.price*self.dict_exchange_rate[index_price.currency].rate 
                res.append(price_in_domestic)

        for curr_name in EnumCurrency :

            if curr_name != EnumCurrency.EUR : 
                r_f = self.dict_interest_rate[curr_name].rate # TODO : r_f se trouve dans FinancialParam 
                value = self.dict_exchange_rate[curr_name].rate #*np.exp(self.t*r_f)
                res.append(value)
                
        return res 


    def display_info(self):
        
        print(f"=========== t = {self.date} =========")
        
        for key in self.dict_index_price.keys() :
            print(f'\t the price of index {key.value} is : {self.dict_index_price[key].price} ')

        for key in self.dict_interest_rate.keys() :
            print(f'\t the intersat rate of  {key.value} is : {self.dict_interest_rate[key].rate} ')
        
        for key in self.dict_exchange_rate.keys() :
            print(f'\t the exchange rate  of  {key.value} to EUR is : {self.dict_exchange_rate[key].rate} ')




