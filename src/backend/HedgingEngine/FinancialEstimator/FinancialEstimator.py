from backend.HedgingEngine.FinancialEstimator.VolatilityEstimator import VolatilityEstimator
from backend.HedgingEngine.FinancialEstimator.CorrelationMatrixEstimator import CorrelationMatrixEstimator
from backend.HedgingEngine.FinancialEstimator.RiskFreeRateEstimator import RiskFreeRateEstimator

from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader 
import numpy as np  
from typing import Dict

class FinancialEstimator :

    def __init__(self , marketDataReader : MarketDataReader ):
        self.volatilityEstimator : VolatilityEstimator = VolatilityEstimator()
        self.riskFreeEstimator : RiskFreeRateEstimator = RiskFreeRateEstimator()
        self.corrMatrixEstimator : CorrelationMatrixEstimator = CorrelationMatrixEstimator()
        self.marketDataReader = marketDataReader

        # self.dict_interest_rate : Dict[EnumCurrency , float] = self.estimate_dict_interest_rate()
        # self.dict_volatility_exchange_rate : Dict[EnumCurrency , float] = self.estimate_dict_volatility_exchange_rate()
        # self.dict_volatility_price : Dict[EnumIndex , float] = self.estimate_dict_volatility_price()
        # self.matrix_corr = self.estimate_matrix_corr()



    def estimate_dict_interest_rate(self) -> Dict[EnumCurrency , float] :
        
        dict_interest_rate = {}

        # TODO : changer ceci : il faut utiliser le current_rate

        # list_interest_rate = self.marketDataReader.get_current_rate(date)


        # for interest_rate in list_interest_rate :
        #     dict_interest_rate[interest_rate.currency] = interest_rate.rate # log(1 + interest_rate.rate) # TODO : check if we need to use log(1 + interest_rate.rate) or not

        # return dict_interest_rate
    
    
        for curr_name in EnumCurrency : 

            list_interest_rate = self.marketDataReader._interest_rate_history.get_all_rate_by_curr_name(curr_name)
            rate_f = self.riskFreeEstimator.mean_estimate(list_interest_rate)

            dict_interest_rate[curr_name] = rate_f
        return dict_interest_rate
    


    
    def estimate_dict_volatility_exchange_rate(self):
        
        dict_volatility = {}

        for curr_name in EnumCurrency : 

            if curr_name != EnumCurrency.EUR :

                list_exchange_rate = self.marketDataReader._exchange_rate_history.get_all_rate_by_currency_name(curr_name)
                volatility_f = self.volatilityEstimator.estimate_volatility(list_exchange_rate)
                dict_volatility[curr_name] = volatility_f
            else :
                dict_volatility[curr_name] = 0.0

        return dict_volatility



    def estimate_dict_volatility_price(self) :
        
        dict_volatility = {}

        for index_name in EnumIndex  : 

            list_price = self.marketDataReader._index_price_history.get_all_price_by_index_name(index_name)
            volatility_f = self.volatilityEstimator.estimate_volatility(list_price)
            dict_volatility[index_name] = volatility_f

        return dict_volatility

    def estimate_matrix_corr(self) :
        
        matrix_index = np.array(self.marketDataReader._index_price_history.get_all_price_for_all_index_name())
        matrix_exchange_rate = np.array(self.marketDataReader._exchange_rate_history.get_all_rate_for_all_curr_name())
        # TODO : fix  matrix_exchange_rate[: ,:matrix_index.shape[1] and remplace that by marketdateReeader.filter_common_valid_dates() ?? 

        matrix = np.vstack((matrix_index, matrix_exchange_rate[: ,:matrix_index.shape[1]]))

        return self.corrMatrixEstimator.estimate_correlation_matrix(matrix)
