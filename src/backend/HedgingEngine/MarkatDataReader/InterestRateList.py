from dataclasses import dataclass
from typing import List, Optional
from backend.HedgingEngine.MarkatDataReader.InterestRate import InterestRate
from backend.HedgingEngine.MarkatDataReader.GenericList import GenericList 
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency



# Liste des taux d'intérêt
class InterestRateList(GenericList[InterestRate]):
    """
    A specialized list for InterestRate objects.
    """


    def get_rate_by_curr_name(self , curr_name : EnumCurrency ):

        for rate in self.items :
            if rate.currency == curr_name :
                return rate.rate
        return None 





