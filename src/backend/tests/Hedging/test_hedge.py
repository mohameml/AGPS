import os
import pandas as pd 
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.Hedging.Hedger import Hedging
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator
from backend.HedgingEngine.Portfolio.PortfolioData import PortfolioData



BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)


"""
============= test hedge  =============
- le test ce fait avec le ServerCpp : 
- il faut lancer au début le server cpp : 
    - cd src/backend/HedgingEngine/Pricer/serverCpp
    - mkdir build
    - cd build
    - cmake -DCMAKE_PREFIX_PATH=/path/to/protoc ..
    - make
    - ./prcing_server
"""


def test_hedger():

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


    portfolioData = PortfolioData(cash=0.0, compos= {
        "EUROSTOXX50": 0.0, 
        "SP500": 0.0, 
        "FTSE100": 0.0, 
        "TOPIX": 0.0, 
        "ASX200": 0.0 , 
        "USD": 0.0, "GBP": 0.0, 
        "JPY": 0.0, 
        "AUD": 0.0}, 
        date=pd.to_datetime('01-05-2009', format='%d-%m-%Y'), isFirstTime=True)
    
    output, portfolio = hedge_engine.hedge(pd.to_datetime('01-05-2009', format='%d-%m-%Y'), portfolioData)

    # print(output)
    # print(portfolio.cash)
    # print(portfolio.compositions)
    # print(portfolio.date)
    # print(portfolio.value)

    # OutputData(date=Timestamp('2009-05-01 00:00:00'), value=100.0, deltas=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], deltas_std_dev=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], price=100.0, price_std_dev=2.0)
    # 100.0
    # {'EUROSTOXX50': 0.0, 'SP500': 0.0, 'FTSE100': 0.0, 'TOPIX': 0.0, 'ASX200': 0.0, 'USD': 0.0, 'GBP': 0.0, 'JPY': 0.0, 'AUD': 0.0}
    # 2009-05-01 00:00:00
    # 100.0

    # assert output.date == pd.to_datetime('01-05-2009', format='%d-%m-%Y')
    # assert output.value == 100.0
    
    # assert output is not None
    # assert portfolio is not None

    # assert len(output.deltas) == 9
    # assert len(output.deltas_std_dev) == 9

    # assert portfolio.date == pd.to_datetime('01-05-2009', format='%d-%m-%Y')



test_hedger()