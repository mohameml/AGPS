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

        if len(list_prices) == 0:
            raise ValueError("La liste des prix ne doit pas être vide.")
        
        if len(list_prices) == 1:
            return np.array([[1.0]])

        # le cas ou il y'a un actif de prix qui ne change pas : 
        for prices in list_prices:
            if np.all(prices == prices[0]):
                raise ValueError("Les prix des actifs ne doivent pas être constants.")

        log_returns = []

        for prices in list_prices:
            log_returns.append(np.log(np.array(prices[1:]) / np.array(prices[:-1])))
        
        log_returns_matrix = np.array(log_returns)
        
        correlation_matrix  = np.round(np.corrcoef(log_returns) , decimals=2)  # np.corrcoef(log_returns_matrix)
        
        # np.cov(log_returns_matrix)

        return correlation_matrix
