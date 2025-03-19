import os
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex
from backend.HedgingEngine.Pricer.PricerGrpc import PricerGrpc
from backend.HedgingEngine.Pricer.PricingParams import PricingParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader

from typing import List 
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from datetime import datetime
import pandas as pd 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)


"""
============= test Grpc connecttion  =============
- le test ce fait avec le ServerCpp : 
- il faut lancer au début le server cpp : 
    - cd src/backend/HedgingEngine/Pricer/serverCpp
    - mkdir build
    - cd build
    - cmake -DCMAKE_PREFIX_PATH=/path/to/protoc ..
    - make
    - ./prcing_server
"""

def test_grpc_conn():

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

    fincail_estimation = FinancialEstimator(reader)
    finance_params = FinancialParams(fincail_estimation , T0 , T , dates_cibles)

    pricerGrpc = PricerGrpc(finance_params)

    msg = pricerGrpc.hello_world()

    # assert msg == "Hello from gRPC Pricer Server!"

    print("test_grpc_conn passed" , msg)


test_grpc_conn()



