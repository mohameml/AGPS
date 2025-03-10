from typing import List, Dict
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency

class PricingResults:
    
    def __init__(self, deltas: List[float], price: float, deltas_std_dev: List[float], price_std_dev: float):

        self.deltas: Dict[str, float] = {}
        self.deltas_std_dev: Dict[str, float] = {}
        self.price: float = price
        self.price_std_dev: float = price_std_dev


        i = 0 
        for index_name in EnumIndex : 
            self.deltas[index_name.value] = deltas[i]
            self.deltas_std_dev[index_name.value] = deltas_std_dev[i]
            i+=1 

        for curr_name in EnumCurrency : 
            if curr_name != EnumCurrency.EUR : 
                self.deltas[curr_name.value]  =  deltas[i]
                self.deltas_std_dev[curr_name.value] = deltas_std_dev[i]
                i+=1

    def display_info(self):
        print(f"Price : {self.price}")
        print(f"Price std dev : {self.price_std_dev}")
        for key in self.deltas.keys():
            print(f"{key} : {self.deltas[key]}")
            print(f"{key} std dev : {self.deltas_std_dev[key]}")
        print("\n")
