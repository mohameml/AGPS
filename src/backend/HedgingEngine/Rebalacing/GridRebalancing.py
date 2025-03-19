from backend.HedgingEngine.Rebalacing.Rebalacing import Rebalancing
from datetime import datetime


class GridRebalancing(Rebalancing):
    def __init__(self, grid_points ):
        self.grid_points = grid_points

    def is_rebalancing(self, date: datetime) -> bool:
        # Implémentation spécifique pour GridRebalancing
        return  date in self.grid_points
