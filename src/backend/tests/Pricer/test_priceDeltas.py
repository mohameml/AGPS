import os
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex
from backend.HedgingEngine.Pricer.PricerGrpc import PricerGrpc
from backend.HedgingEngine.Pricer.PricingParams import PricingParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialParam.ListDataFeed import ListDataFeed
from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter


from typing import List 
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from datetime import datetime
import pandas as pd 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)


"""
============= test Grpc price and deltas =============
- le test ce fait avec le ServerCpp : 
- il faut lancer au début le server cpp : 
    - cd src/backend/HedgingEngine/Pricer/serverCpp
    - mkdir build
    - cd build
    - cmake -DCMAKE_PREFIX_PATH=/path/to/protoc ..
    - make
    - ./prcing_server
"""


def get_financial_params():
    
    indexes = [
        EnumIndex.ASX200 , 
        EnumIndex.EUROSTOXX50 ,
        EnumIndex.FTSE100 ,
        EnumIndex.SP500 ,
        EnumIndex.TOPIX
    ]
    
    dates_cibles = [
        pd.to_datetime('01-04-2010', format="%d-%m-%Y"),
        pd.to_datetime('01-04-2011', format="%d-%m-%Y"),
        pd.to_datetime('01-04-2012', format="%d-%m-%Y"),
        pd.to_datetime('01-04-2013', format="%d-%m-%Y"),
    ]

    T0 = pd.to_datetime('01-05-2009' , format='%d-%m-%Y')
    T = pd.to_datetime('01-06-2014', format='%d-%m-%Y')

    marketDataReader = MarketDataReader(FILE_PATH , indexes , T0 , T)
    financialEstimator = FinancialEstimator(marketDataReader)
    finance_params = FinancialParams(financialEstimator ,  T0 , T , dates_cibles)

    return finance_params


def test_grpc_price_and_deltas():

    indexes = [
        EnumIndex.ASX200 , 
        EnumIndex.EUROSTOXX50 ,
        EnumIndex.FTSE100 ,
        EnumIndex.SP500 ,
        EnumIndex.TOPIX
    ]
    
    dates_cibles = [
        pd.to_datetime('01-04-2010', format="%d-%m-%Y"),
        pd.to_datetime('01-04-2011', format="%d-%m-%Y"),
        pd.to_datetime('01-04-2012', format="%d-%m-%Y"),
        pd.to_datetime('01-04-2013', format="%d-%m-%Y"),
    ]

    T0 = pd.to_datetime('01-05-2009' , format='%d-%m-%Y')
    T = pd.to_datetime('01-06-2014', format='%d-%m-%Y')

    
    reader  = MarketDataReader(FILE_PATH , indexes , T0 , T)

    finance_params = get_financial_params()

    pricerGrpc = PricerGrpc(finance_params)

    data_feed_t0 = reader.get_data_feed(T0)
    converter = MathDateConverter(finance_params.nombreOfDaysInOneYear , T0)
    past = ListDataFeed(finance_params)
    past.addDataFeed(data_feed_t0)
    monitoring_date = False
    time_math = converter.ConvertToMathDistance(T0, data_feed_t0.date)
    pricer_params = PricingParams(past, time_math, monitoring_date)

    print(pricer_params)

    # res = pricerGrpc.price_and_deltas(pricer_params)
    # print(res)


    #   Price : 100.0
    # Price std dev : 2.0
    # EUROSTOXX50 : 0.0
    # EUROSTOXX50 std dev : 0.0
    # SP500 : 0.0
    # SP500 std dev : 0.0
    # FTSE100 : 0.0
    # FTSE100 std dev : 0.0
    # TOPIX : 0.0
    # TOPIX std dev : 0.0
    # ASX200 : 0.0
    # ASX200 std dev : 0.0
    # USD : 0.0
    # USD std dev : 0.0
    # GBP : 0.0
    # GBP std dev : 0.0
    # JPY : 0.0
    # JPY std dev : 0.0
    # AUD : 0.0
    # AUD std dev : 0.0

    # assert res.price == 100.0
    # assert res.price_std_dev == 2.0
    # assert res.deltas['EUROSTOXX50'] == 0.0
    # assert res.deltas['SP500'] == 0.0
    # assert res.deltas['FTSE100'] == 0.0
    # assert res.deltas['TOPIX'] == 0.0
    # assert res.deltas['ASX200'] == 0.0
    # assert res.deltas['USD'] == 0.0
    # assert res.deltas['GBP'] == 0.0
    # assert res.deltas['JPY'] == 0.0
    # assert res.deltas['AUD'] == 0.0

    # res.display_info()








test_grpc_price_and_deltas()