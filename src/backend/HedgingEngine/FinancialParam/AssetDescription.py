import numpy as np 
from typing import List , Dict
from backend.HedgingEngine.FinancialParam.Asset import Asset
from backend.HedgingEngine.FinancialParam.Currency import Currency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator




class  AssetDescription :

    def __init__(self ,  financialEstimator : FinancialEstimator) :
        
        self.domesticCurrencyId = "EUR"
        self.matrix_corr = np.zeros((9,9))
        self.assets : List[Asset]= []
        self.currencies : List[Currency] =  []
        self.estimate_params(financialEstimator);

        

    def estimate_params(self  , financialEstimator : FinancialEstimator):


        for index_name , volatility in financialEstimator.dict_volatility_price.items() : 
            self.assets.append(Asset(index_name , volatility))

        for curr_name in financialEstimator.dict_volatility_exchange_rate.keys() :
            volatility = financialEstimator.dict_volatility_exchange_rate[curr_name]
            rate = financialEstimator.dict_interest_rate[curr_name]
            self.currencies.append(Currency(curr_name , volatility , rate))


        self.matrix_corr = financialEstimator.matrix_corr


    def get_rate_of_domesitc_currency(self) -> float :
        
        for curr in self.currencies : 
            if curr.id.value == self.domesticCurrencyId :
                return curr.rate

        return 0.0

    def get_dict_interset_rate_estimate(self):

        dict_interset : Dict[EnumCurrency , float] = {}

        for curr in self.currencies :
            dict_interset[curr.id]  = curr.rate

        return dict_interset

    def display_info(self):

        print(f"domesticCurrencyId = {self.domesticCurrencyId}")
        print(f"matrix_corr = \n")
        print(self.matrix_corr)

        for asset in self.assets : 
            asset.display_info()
        
        for curr in self.currencies : 
            curr.display_info()