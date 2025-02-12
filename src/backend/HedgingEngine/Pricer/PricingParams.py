from typing import List
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed


class PricingParams :

    def __init__(self, data : List[DataFeed], time : float, monitoring_date : bool):

        self.data_feeds = data
        self.time = time
        self.monitoring_date = monitoring_date

    def set_params(self, data: List[DataFeed], time: float, monitoring_date: bool):
        self.data_feeds = data
        self.time = time
        self.monitoring_date = monitoring_date
