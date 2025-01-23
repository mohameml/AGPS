from backend.HedgingEngine.MarkatDataReader.GenericList import GenericList
from backend.HedgingEngine.MarkatDataReader.ExchangeRate import ExchangeRate
from types import List 

# Liste des taux de change
class ExchangeRateList(GenericList[ExchangeRate]):
    """
    A specialized list for ExchangeRate objects.
    """
