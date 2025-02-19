from typing import List, Dict
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency

class PricingResults:
    
    def __init__(self, deltas: List[float], price: float, deltas_std_dev: List[float], price_std_dev: float):

        self.deltas: Dict[str, float] = {}
        self.deltas_std_dev: Dict[str, float] = {}
        self.price: float = price
        self.price_std_dev: float = price_std_dev


        # TODO  : FIX cette partie  
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


        # for i in range(len(deltas)):
        #     self.deltas[ids[i]] = deltas[i]
        #     self.deltas_std_dev[ids[i]] = deltas_std_dev[i]
