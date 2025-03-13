import os 
import pandas as pd 
from backend.HedgingEngine.Hedging.Hedger import Hedging
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator



BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "./data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)


indexes = [
    EnumIndex.ASX200 , 
    EnumIndex.EUROSTOXX50 ,
    EnumIndex.FTSE100 ,
    EnumIndex.SP500 ,
    EnumIndex.TOPIX
]



dates_versement = [
    pd.to_datetime('01-04-2010', format="%d-%m-%Y"),
    pd.to_datetime('01-04-2011', format="%d-%m-%Y"),
    pd.to_datetime('01-04-2012', format="%d-%m-%Y"),
    pd.to_datetime('01-04-2013', format="%d-%m-%Y"),
]

T0 = pd.to_datetime('01-05-2009' , format='%d-%m-%Y')
T = pd.to_datetime('01-06-2010', format='%d-%m-%Y')



# MarketDataReader : interface pour lire les données de marché
market_data_reader = MarketDataReader(FILE_PATH , indexes , T0 , T)

# financial_estimator : estimateur financier
financialEstimator = FinancialEstimator(market_data_reader)

# FinancialParams : paramètres financiers
financial_params = FinancialParams(financialEstimator,  T0, T , dates_versement)


# hedge_engine : moteur de couverture
hedge_engine = Hedging(financial_params)


def get_market_data_reader():
    return market_data_reader


def get_hedge_engine():
    return hedge_engine


