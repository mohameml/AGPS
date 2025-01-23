# from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
# from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex

from datetime import datetime 
import pandas as pd

from ..HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from ..HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex


FILE_PATH = "../data/DonneesGPS2025.xlsx"

def test_1() :

    indexes = [
        EnumIndex.ASX200 , 
        EnumIndex.EUROSTOXX50 ,
        EnumIndex.FTSE100 ,
        EnumIndex.SP500 ,
        EnumIndex.TOPIX
    ]

    #  'T0': '01-05-2009',
    # 'T1': '01-04-2010',
    # 'T2': '01-04-2011',
    # 'T3': '01-04-2012',
    # 'T4': '01-04-2013',
    # 'Tc': '01-06-2014'

    T0 = pd.to_datetime('01-05-2009' , format='%d-%m-%Y')
    T = pd.to_datetime('01-06-2010', format='%d-%m-%Y')
    reader : MarketDataReader = MarketDataReader( FILE_PATH , indexes , T0 , T)
    reader._index_price_history.display_info()