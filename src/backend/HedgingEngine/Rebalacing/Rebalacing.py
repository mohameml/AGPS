from datetime import datetime
from abc import ABC, abstractmethod



class Rebalancing(ABC):

    @abstractmethod
    def is_rebalancing(self, date: datetime) -> bool:
        pass

    @staticmethod
    def create_rebalancing(rebalancing_type: str, *args, **kwargs):
        from backend.HedgingEngine.Rebalacing.FixedRebalacing import FixedRebalancing
        from backend.HedgingEngine.Rebalacing.GridRebalancing import GridRebalancing

        if rebalancing_type == "FixedRebalancing":
            return FixedRebalancing(*args, **kwargs)
        elif rebalancing_type == "GridRebalancing":
            return GridRebalancing(*args, **kwargs)
        else:
            raise ValueError("Unknown rebalancing type")

