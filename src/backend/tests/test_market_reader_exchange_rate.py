import os
import pandas as pd
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex



BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)


def test_reader() :

    indexes = [
        EnumIndex.ASX200 , 
        EnumIndex.EUROSTOXX50 ,
        EnumIndex.FTSE100 ,
        EnumIndex.SP500 ,
        EnumIndex.TOPIX
    ]
    

    T0 = pd.to_datetime('01-05-2009' , format='%d-%m-%Y')
    T = pd.to_datetime('01-06-2009', format='%d-%m-%Y')
    reader : MarketDataReader = MarketDataReader(FILE_PATH , indexes , T0 , T)
    reader._exchange_rate_history.display_info()


test_reader()





