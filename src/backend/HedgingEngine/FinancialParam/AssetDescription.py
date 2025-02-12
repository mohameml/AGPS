import numpy as np 
from typing import List
from backend.HedgingEngine.FinancialParam.Asset import Asset
from backend.HedgingEngine.FinancialParam.Currency import Currency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialEstimator.VolatilityEstimator import VolatilityEstimator
from backend.HedgingEngine.FinancialEstimator.CorrelationMatrixEstimator import CorrelationMatrixEstimator
from backend.HedgingEngine.FinancialEstimator.RiskFreeRateEstimator import RiskFreeRateEstimator


class  AssetDescription :

    def __init__(self ):
        
        self.domesticCurrencyId = "EUR"
        self.matrix_corr = np.zeros((5,5))
        self.assets : List[Asset]= []
        self.currencies : List[Currency] =  []
        self.volatilityEstimator : VolatilityEstimator = VolatilityEstimator()
        self.riskFreeEstimator : RiskFreeRateEstimator = RiskFreeRateEstimator()
        self.corrMatrixEstimator : CorrelationMatrixEstimator = CorrelationMatrixEstimator()
        


    def estimate_params(self , marketDataReader : MarketDataReader):

        # 1) on commance par assets :

        for index_name in  EnumIndex : 

            list_price = marketDataReader._index_price_history.get_all_price_by_index_name(index_name)
            volatility = self.volatilityEstimator.estimate_volatility(list_price)
            self.assets.append(Asset(index_name , volatility))

        for curr_name in EnumCurrency : 

            list_exchange_rate = marketDataReader._exchange_rate_history.get_all_rate_by_currency_name(curr_name)
            rate_f = self.riskFreeEstimator.mean_estimate(list_exchange_rate)
            volatility_f = self.volatilityEstimator.estimate_volatility(list_exchange_rate)
            self.currencies.append(Currency(curr_name , volatility_f , rate_f))

        matrix_index = marketDataReader._index_price_history.get_all_price_for_all_index_name()

        matrix_exchange_rate = marketDataReader._exchange_rate_history.get_all_rate_by_currency_name()

        matrix = np.vstack((np.array(matrix_index) , np.array(matrix_exchange_rate)))

        self.matrix_corr = self.corrMatrixEstimator.estimate_correlation_matrix(matrix)

    def display_info(self):

        print(f"domesticCurrencyId = {self.domesticCurrencyId}")
        print(f"matrix_corr = \n")
        print(self.matrix_corr)

        for asset in self.assets : 
            asset.display_info()
        
        for curr in self.currencies : 
            curr.display_info()