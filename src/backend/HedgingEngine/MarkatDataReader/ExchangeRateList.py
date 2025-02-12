from backend.HedgingEngine.MarkatDataReader.GenericList import GenericList
from backend.HedgingEngine.MarkatDataReader.ExchangeRate import ExchangeRate
# from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency



from typing import List 

# Liste des taux de change
class ExchangeRateList(GenericList[ExchangeRate]):
    """
    A specialized list for ExchangeRate objects.
    """


    def get_rate_by_currency_name(self , curr_name : EnumCurrency) :

        for exchange_rate in self.items : 
            if exchange_rate.base_currency == curr_name : 
                return exchange_rate.rate
            
        return None 