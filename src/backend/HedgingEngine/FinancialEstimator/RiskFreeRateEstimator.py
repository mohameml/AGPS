from typing import List
import numpy as np

class RiskFreeRateEstimator:

    def __init__(self):
        """
        Classe pour estimer le taux d'intérêt sans risque r à partir d'une liste de taux r_t.
        """


    def mean_estimate(self , r_t : List[float]) -> float:
        """ Estimation par la moyenne historique. """
        return np.mean(r_t)



