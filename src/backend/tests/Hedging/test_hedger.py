import os
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex
from backend.HedgingEngine.Pricer.PricerGrpc import PricerGrpc
from backend.HedgingEngine.Pricer.PricingParams import PricingParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.Hedging.Hedger import Hedging

from typing import List 
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from datetime import datetime
import pandas as pd 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)

def test_hedger():

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
    T = pd.to_datetime('01-06-2010', format='%d-%m-%Y')

    
    reader  = MarketDataReader(FILE_PATH , indexes , T0 , T)

    finance_params = FinancialParams(FILE_PATH , indexes , T0 , T , dates_cibles)

    hedger = Hedging(finance_params)

    list_output = hedger.hedge(reader.get_all_data_feed())

    for output in list_output:
        print(output)



test_hedger()