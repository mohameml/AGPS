from datetime import datetime
from backend.HedgingEngine.Rebalacing.Rebalacing import Rebalancing

class FixedRebalancing(Rebalancing):
    def __init__(self, periode: int):
        self.periode = periode
        self.count = 1

    def is_rebalancing(self, date: datetime) -> bool:

        if self.count == self.periode :
            self.count = 1
            return True
        self.count += 1
        return False