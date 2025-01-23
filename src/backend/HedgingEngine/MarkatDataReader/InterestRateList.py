from dataclasses import dataclass
from typing import List, Optional
from backend.HedgingEngine.MarkatDataReader.InterestRate import InterestRate
from backend.HedgingEngine.MarkatDataReader.GenericList import GenericList 



# Liste des taux d'intérêt
class InterestRateList(GenericList[InterestRate]):
    """
    A specialized list for InterestRate objects.
    """
    pass





