from typing import List
import numpy as np

class VolatilityEstimator:

    def __init__(self, list_price: List[float] , trading_days_per_year : int = 252):

        self.list_price: List[float] = list_price
        self.volatility: float = self.estimate_volatility(True , trading_days_per_year)

    def estimate_volatility(self, annualize: bool = False, trading_days_per_year: int = 252) -> float:
        """
        - Calcule la volatilité de l'indice en utilisant les rendements logarithmiques.
        
        - annualize: Si True, annualise la volatilité. Par défaut False.
        - trading_days_per_year: Nombre de jours de bourse par an, par défaut 252.
        - return  :Volatilité estimée.
        """
        

        log_returns = np.log(np.array(self.list_price[1:]) / np.array(self.list_price[:-1]))


        volatility_daily = np.std(log_returns)

        if annualize:
            volatility_annualized = volatility_daily * np.sqrt(trading_days_per_year)
            return volatility_annualized
        else:
            return volatility_daily

