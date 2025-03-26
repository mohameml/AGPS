from typing import List
import numpy as np

class RiskFreeRateEstimator:

    def __init__(self):
        """
        Classe pour estimer le taux d'intérêt sans risque r à partir d'une liste de taux r_t.
        """


    def mean_estimate(self , r_t : List[float]) -> float:
        """ Estimation par la moyenne historique. """
        if len(r_t) == 0:
            raise ValueError("La liste des taux r_t ne peut pas être vide.")

        return np.mean(r_t) # log(1+ r_t) = r_t



