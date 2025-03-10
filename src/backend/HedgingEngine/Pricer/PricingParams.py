from typing import List
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from backend.HedgingEngine.FinancialParam.ListDataFeed import ListDataFeed

class PricingParams :

    def __init__(self, data : ListDataFeed, time : float, monitoring_date : bool):

        self.data_feeds = data
        self.time = time
        self.monitoring_date = monitoring_date

    def set_params(self, data:ListDataFeed, time: float, monitoring_date: bool):
        self.data_feeds = data
        self.time = time
        self.monitoring_date = monitoring_date
