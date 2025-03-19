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


    def __init__(
        self, 
        date: datetime, 
        dict_index_price: Dict[EnumIndex, IndexPrice], 
        dict_exchange_rate: Dict[EnumCurrency, ExchangeRate],
    ):
        self.date = date
        self.dict_index_price = dict_index_price
        self.dict_exchange_rate = dict_exchange_rate


    def toDomesticMarket(self , dict_interest_rate : Dict[EnumCurrency , float] , converter : MathDateConverter):
        res = []

        for index_name in EnumIndex :

            if index_to_currency[index_name] == EnumCurrency.EUR :
                res.append(self.dict_index_price[index_name].price) # S0_t0
            else : 
                index_price = self.dict_index_price[index_name]
                price_in_domestic  = index_price.price*self.dict_exchange_rate[index_price.currency].rate 
                res.append(price_in_domestic)

        for curr_name in EnumCurrency :

            if curr_name != EnumCurrency.EUR : 
                r_f = dict_interest_rate[curr_name] 
                t = converter.ConvertToMathDistance(self.date)
                value = self.dict_exchange_rate[curr_name].rate*np.exp(t*r_f)
                res.append(float(value))
                
        return res 

    def get_spot_list(self , dict_interest_rate : Dict[EnumCurrency , float] , converter : MathDateConverter) -> Dict[str , float] :

        """
        retourne un dict avce les prices en marche domestique  : utilise en portfolio [RQ : curr_name est utilise ici pour le ZC du marche étranger ]
        """

        spot_list = {}

        res = self.toDomesticMarket(dict_interest_rate , converter)

        i = 0 
        for index_name in EnumIndex : 
            spot_list[index_name.value] = res[i]
            i+=1 

        for curr_name in EnumCurrency : 
            if curr_name != EnumCurrency.EUR : 
                spot_list[curr_name.value]  =  res[i]
                i+=1

        return spot_list


    def display_info(self):
        
        print(f"=========== t = {self.date} =========")
        
        for key in self.dict_index_price.keys() :
            print(f'\t the price of index {key.value} is : {self.dict_index_price[key].price} ')

        
        for key in self.dict_exchange_rate.keys() :
            print(f'\t the exchange rate  of  {key.value} to EUR is : {self.dict_exchange_rate[key].rate} ')
        




