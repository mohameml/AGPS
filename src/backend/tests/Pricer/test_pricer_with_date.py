import os
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.Hedging.Hedger import Hedging
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex
from backend.HedgingEngine.Portfolio.PortfolioData import PortfolioData
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




def test_grpc_price_and_deltas():

    indexes = [
        EnumIndex.ASX200 , 
        EnumIndex.EUROSTOXX50 ,
        EnumIndex.FTSE100 ,
        EnumIndex.SP500 ,
        EnumIndex.TOPIX
    ]
    
    # dates_cibles = [
    #     pd.to_datetime('03-07-2001', format="%d-%m-%Y"),
    #     pd.to_datetime('02-07-2002', format="%d-%m-%Y"),
    #     pd.to_datetime('02-07-2003', format="%d-%m-%Y"),
    #     pd.to_datetime('02-07-2004', format="%d-%m-%Y"),
    # ]

    # T0 = pd.to_datetime('05-07-2000' , format='%d-%m-%Y')
    # T = pd.to_datetime('05-07-2005', format='%d-%m-%Y')
    

    dates_cibles = [
        pd.to_datetime('04-01-2010', format="%d-%m-%Y"),
        pd.to_datetime('04-01-2011', format="%d-%m-%Y"),
        pd.to_datetime('04-01-2012', format="%d-%m-%Y"),
        pd.to_datetime('04-01-2013', format="%d-%m-%Y"),
    ]

    T0 = pd.to_datetime('05-01-2009' , format='%d-%m-%Y')
    T = pd.to_datetime('06-01-2014', format='%d-%m-%Y')


    
    reader  = MarketDataReader(FILE_PATH , indexes , T0 , T)
    financialEstimator = FinancialEstimator(reader)
    finance_params = FinancialParams(financialEstimator ,  T0 , T , dates_cibles)

    hedge_engine = Hedging(finance_params)

    portfolioData = PortfolioData(
        cash=0.0, 
        compos= {
            "EUROSTOXX50": 0.0, 
            "SP500": 0.0, 
            "FTSE100": 0.0, 
            "TOPIX": 0.0, 
            "ASX200": 0.0 , 
            "USD": 0.0, "GBP": 0.0, 
            "JPY": 0.0, 
            "AUD": 0.0
        }, 
        date=T0, 
        isFirstTime=True
    )

    # date = pd.to_datetime('01-04-2010', format='%d-%m-%Y') # changer date pour tester Pricer à une autre date 

    output, portfolio = hedge_engine.hedge(T0, portfolioData)



test_grpc_price_and_deltas()