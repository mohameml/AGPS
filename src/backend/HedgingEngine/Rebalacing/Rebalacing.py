from datetime import datetime
from abc import ABC, abstractmethod


class Rebalancing(ABC):
    @abstractmethod
    def is_rebalancing(self, date: datetime) -> bool:
        pass

    @staticmethod
    def create_rebalancing(rebalancing_type: str, *args, **kwargs):
        if rebalancing_type == "FixedRebalancing":
            return FixedRebalancing(*args, **kwargs)
        elif rebalancing_type == "GridRebalancing":
            return GridRebalancing(*args, **kwargs)
        else:
            raise ValueError("Unknown rebalancing type")

class FixedRebalancing(Rebalancing):
    def __init__(self, period):
        self.period = period

    def is_rebalancing(self, date: datetime) -> bool:
        # Implémentation spécifique pour FixedRebalancing
        pass

class GridRebalancing(Rebalancing):
    def __init__(self, grid_points):
        self.grid_points = grid_points

    def is_rebalancing(self, date: datetime) -> bool:
        # Implémentation spécifique pour GridRebalancing
        pass
