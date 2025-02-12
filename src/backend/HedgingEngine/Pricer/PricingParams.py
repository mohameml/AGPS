from typing import List

class DataFeed:
    # Définir la classe DataFeed en fonction de vos besoins
    pass

class PricingParams:
    
    def __init__(self, data: List[DataFeed], time: float, monitoring_date: bool):
        self.data_feeds = data
        self.time = time
        self.monitoring_date = monitoring_date
    
    def set_params(self, data: List[DataFeed], time: float, monitoring_date: bool):
        self.data_feeds = data
        self.time = time
        self.monitoring_date = monitoring_date
