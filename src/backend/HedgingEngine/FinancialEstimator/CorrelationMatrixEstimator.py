from typing import List
import numpy as np

class CorrelationMatrixEstimator:

    def __init__(self):
        """
        - list_prices: Liste des prix pour chaque actif.
        """

    def estimate_correlation_matrix(self , list_prices: np.ndarray) -> np.ndarray:
        """
        Calcule la matrice de corrélation entre plusieurs actifs en utilisant les rendements logarithmiques.
        """

        log_returns = []

        for prices in list_prices:
            log_returns.append(np.log(np.array(prices[1:]) / np.array(prices[:-1])))
        
        log_returns_matrix = np.array(log_returns)
        
        correlation_matrix = np.corrcoef(log_returns_matrix)
        
        return correlation_matrix
