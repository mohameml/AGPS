import numpy as np 
from typing import List , Dict
from backend.HedgingEngine.FinancialParam.Asset import Asset
from backend.HedgingEngine.FinancialParam.Currency import Currency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator




class  AssetDescription :

    def __init__(self ):
        
        self.domesticCurrencyId = "EUR"
        self.matrix_corr = np.zeros((5,5))
        self.assets : List[Asset]= []
        self.currencies : List[Currency] =  []
        self.financialEstimator : FinancialEstimator = FinancialEstimator()

        

    def estimate_params(self , marketDataReader : MarketDataReader):


        # 1) Estimation de la volatilite de chaque index : 

        for index_name in  EnumIndex : 

            list_price = marketDataReader._index_price_history.get_all_price_by_index_name(index_name)
            volatility = self.financialEstimator.volatilityEstimator.estimate_volatility(list_price)
            self.assets.append(Asset(index_name , volatility))

        # 2) Estimation de la volatilite et de taux r_f de chaque Taux de Change : 

        for curr_name in EnumCurrency : 

            if curr_name != EnumCurrency.EUR :

                list_interest_rate = marketDataReader._interest_rate_history.get_all_rate_by_curr_name(curr_name)
                rate_f = self.financialEstimator.riskFreeEstimator.mean_estimate(list_interest_rate)
                
                list_exchange_rate = marketDataReader._exchange_rate_history.get_all_rate_by_currency_name(curr_name)
                volatility_f = self.financialEstimator.volatilityEstimator.estimate_volatility(list_exchange_rate)
                
                self.currencies.append(Currency(curr_name , volatility_f , rate_f))
            else :

                list_interest_rate = marketDataReader._interest_rate_history.get_all_rate_by_curr_name(curr_name)
                rate_eur = self.financialEstimator.riskFreeEstimator.mean_estimate(list_interest_rate)
                self.currencies.append(Currency(curr_name , 0.0 , rate_eur))

        # 3)  Estimation de la matrice de corrélation : 

        matrix_index = np.array(marketDataReader._index_price_history.get_all_price_for_all_index_name())
        matrix_exchange_rate = np.array(marketDataReader._exchange_rate_history.get_all_rate_for_all_curr_name())
        matrix = np.vstack((matrix_index, matrix_exchange_rate[: ,:matrix_index.shape[1]]))

        self.matrix_corr = self.financialEstimator.corrMatrixEstimator.estimate_correlation_matrix(matrix)


    def get_dict_interset_rate_estimate(self):

        dict_interset : Dict[EnumCurrency , float] = {}

        for curr in self.currencies :
            dict_interset[curr.name]  = curr.rate

        return dict_interset

    def display_info(self):

        print(f"domesticCurrencyId = {self.domesticCurrencyId}")
        print(f"matrix_corr = \n")
        print(self.matrix_corr)

        for asset in self.assets : 
            asset.display_info()
        
        for curr in self.currencies : 
            curr.display_info()