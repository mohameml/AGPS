from typing import List
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from backend.HedgingEngine.FinancialParam.ListDataFeed import ListDataFeed
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from typing import Dict

class PricingParams :

    def __init__(self, data : ListDataFeed, time : float, monitoring_date : bool , dict_interest_rate : Dict[EnumCurrency, float]):

        self.data_feeds = data
        self.time = time
        self.monitoring_date = monitoring_date
        self.dict_interest_rate = dict_interest_rate

    def set_params(self, data:ListDataFeed, time: float, monitoring_date: bool  , dict_interest_rate: Dict[EnumCurrency, float]):
        self.data_feeds = data
        self.time = time
        self.monitoring_date = monitoring_date
        self.dict_interest_rate = dict_interest_rate
