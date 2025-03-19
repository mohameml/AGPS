import os
import pandas as pd
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter



BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)


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


def test_get_spot_list() :

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
    # data_feed.display_info()

    finance_params  = get_financial_params()
    converter = MathDateConverter(252 , T0)
    spot = data_feed.get_spot_list(finance_params.assetDescription.get_dict_interset_rate_estimate() , converter)


    assert spot == {'EUROSTOXX50': 2375.34, 'SP500': 661.6300987710171, 'FTSE100': 4772.382774636206, 'TOPIX': 6.444344137367406, 'ASX200': 2075.9374500490085, 'USD': 0.7539772298876574, 'GBP': 1.1247078338234184, 'JPY': 0.007609782295999771, 'AUD': 0.550704968709945}
    
    # {'EUROSTOXX50': 2375.34, 'SP500': 661.6300987710171, 'FTSE100': 4772.382774636206, 'TOPIX': 6.444344137367406, 'ASX200': 2075.9374500490085, 
    # 'USD': 0.7539772298876574, 'GBP': 1.1247078338234184, 'JPY': 0.007609782295999771, 'AUD': 0.550704968709945}

    # print(spot)

# test_get_spot_list()





