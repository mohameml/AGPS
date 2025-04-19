import os
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex, MarketDataReader
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator
import pandas as pd 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)

def test_financial_params():

    indexes = [
        EnumIndex.ASX200 , 
        EnumIndex.EUROSTOXX50 ,
        EnumIndex.FTSE100 ,
        EnumIndex.SP500 ,
        EnumIndex.TOPIX
    ]
    
    dates_cibles = [
        pd.to_datetime('04-01-2010', format="%d-%m-%Y"),
        pd.to_datetime('04-01-2011', format="%d-%m-%Y"),
        pd.to_datetime('04-01-2012', format="%d-%m-%Y"),
        pd.to_datetime('04-01-2013', format="%d-%m-%Y"),
    ]

    T0 = pd.to_datetime('05-01-2009' , format='%d-%m-%Y')
    T = pd.to_datetime('06-01-2014', format='%d-%m-%Y')


    # dates_cibles = [
    #     pd.to_datetime('03-07-2001', format="%d-%m-%Y"),
    #     pd.to_datetime('02-07-2002', format="%d-%m-%Y"),
    #     pd.to_datetime('02-07-2003', format="%d-%m-%Y"),
    #     pd.to_datetime('02-07-2004', format="%d-%m-%Y"),
    # ]

    # T0 = pd.to_datetime('05-07-2000' , format='%d-%m-%Y')
    # T = pd.to_datetime('05-07-2005', format='%d-%m-%Y')
    

    marketDataReader = MarketDataReader(FILE_PATH , indexes , T0 , T)
    financialEstimator = FinancialEstimator(marketDataReader)
    finance_params = FinancialParams(financialEstimator ,  T0 , T , dates_cibles)

    finance_params.to_json("./backend/tests/FinancialParam/finance_params.json")

    dict_interset_rate = marketDataReader.get_current_rate_dict(T0)
    print(dict_interset_rate)
    # if everything is ok, then : 
    # assert True



test_financial_params()