import os
import numpy as np
import pandas as pd
import pytest
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex



BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)


def test_get_data_feed_with_date_valide() :

    indexes = [
        EnumIndex.ASX200 , 
        EnumIndex.EUROSTOXX50 ,
        EnumIndex.FTSE100 ,
        EnumIndex.SP500 ,
        EnumIndex.TOPIX
    ]
    


    T0 = pd.to_datetime('01-05-2009' , format='%d-%m-%Y')
    T = pd.to_datetime('01-06-2014', format='%d-%m-%Y')
    reader : MarketDataReader = MarketDataReader(FILE_PATH , indexes , T0 , T)


    date = pd.to_datetime('01-05-2009' , format = '%d-%m-%Y')
    data_feed = reader.get_data_feed(date)
    data_feed.display_info()

    #   the price of index ASX200 is : 3769.6 
    #  the price of index EUROSTOXX50 is : 2375.34 
    #  the price of index FTSE100 is : 4243.22 
    #  the price of index SP500 is : 877.52 
    #  the price of index TOPIX is : 846.85 
    #  the exchange rate  of  AUD to EUR is : 0.550704968709945 
    #  the exchange rate  of  GBP to EUR is : 1.1247078338234184 
    #  the exchange rate  of  USD to EUR is : 0.7539772298876574 
    #  the exchange rate  of  JPY to EUR is : 0.007609782295999771 

    assert np.isclose(data_feed.dict_index_price[EnumIndex.ASX200].price , 3769.6 , atol=1e-2)
    assert data_feed.dict_index_price[EnumIndex.EUROSTOXX50].price == 2375.34
    assert data_feed.dict_index_price[EnumIndex.FTSE100].price == 4243.22
    assert data_feed.dict_index_price[EnumIndex.SP500].price == 877.52
    assert data_feed.dict_index_price[EnumIndex.TOPIX].price == 846.85

    assert data_feed.dict_exchange_rate[EnumCurrency.AUD].rate == 0.550704968709945
    assert data_feed.dict_exchange_rate[EnumCurrency.GBP].rate == 1.1247078338234184
    assert data_feed.dict_exchange_rate[EnumCurrency.USD].rate == 0.7539772298876574
    assert data_feed.dict_exchange_rate[EnumCurrency.JPY].rate == 0.007609782295999771

def test_get_data_feed_with_date_not_valide() :


    indexes = [
        EnumIndex.ASX200 , 
        EnumIndex.EUROSTOXX50 ,
        EnumIndex.FTSE100 ,
        EnumIndex.SP500 ,
        EnumIndex.TOPIX
    ]
    


    T0 = pd.to_datetime('01-05-2009' , format='%d-%m-%Y')
    T = pd.to_datetime('01-06-2014', format='%d-%m-%Y')
    reader : MarketDataReader = MarketDataReader(FILE_PATH , indexes , T0 , T)


    date = pd.to_datetime('02-05-2009' , format = '%d-%m-%Y')
    
    with pytest.raises(Exception) as e:
        data_feed = reader.get_data_feed(date)
        assert str(e) == "La date {date} n'est pas dans la période d'analyse.".format(date = date)
    



