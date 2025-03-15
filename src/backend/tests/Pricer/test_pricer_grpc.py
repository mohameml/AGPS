import os
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.FinancialParam.ListDataFeed import ListDataFeed
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

def test_financial_params():

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
    
    finance_params = FinancialParams(fincail_estimation, T0 , T , dates_cibles)

    pricerGrpc = PricerGrpc(finance_params)

    data : ListDataFeed = ListDataFeed(finance_params)

    data.addDataFeed(reader.get_data_feed(T0))
    # data.append(reader.get_data_feed(T0))

    time = 0.111 

    prcing_params = PricingParams(data  , time  , True);

    input_data = pricerGrpc.pricing_params_to_pricing_input(prcing_params)

    #    =============== PrcingInput =================
    # past {
    # value: 2375.34
    # value: 661.63009877101706
    # value: 4772.3827746362058
    # value: 6.4443441373674064
    # value: 2075.9374500490085
    # value: 0.75397722988765736
    # value: 1.1247078338234184
    # value: 0.0076097822959997714
    # value: 0.550704968709945
    # }
    # monitoringDateReached: true
    # time: 0.111
    # currencies {
    # id: "EUR"
    # interestRate: 0.0069618778280542987
    # }
    # currencies {
    # id: "USD"
    # interestRate: 0.0041069758672699847
    # volatility: 0.096598910043132771
    # }
    # currencies {
    # id: "GBP"
    # interestRate: 0.0073841251885369526
    # volatility: 0.078170184826813149
    # }
    # currencies {
    # id: "JPY"
    # interestRate: 0.0024464177978883862
    # volatility: 0.12881009473359448
    # }
    # currencies {
    # id: "AUD"
    # interestRate: 0.039447699849170438
    # volatility: 0.10026207344543647
    # }
    # domesticCurrencyId: "EUR"
    # assets {
    # currencyId: "EUROSTOXX50"
    # volatility: 0.23121705813542
    # }
    # assets {
    # currencyId: "SP500"
    # volatility: 0.17758056635452812
    # }
    # assets {
    # currencyId: "FTSE100"
    # volatility: 0.16904759292955523
    # }
    # assets {
    # currencyId: "TOPIX"
    # volatility: 0.21037732628424263
    # }
    # assets {
    # currencyId: "ASX200"
    # volatility: 0.16495413502313466
    # }
    # correlations {
    # values: 1
    # values: 0.71868417702905363
    # values: 0.882600568341162
    # values: 0.23684883754736524
    # values: 0.3425406456087533
    # values: 0.06382582934715679
    # values: 0.044086617067059207
    # values: 0.040928131400150565
    # values: 0.040303062059497748
    # }
    # correlations {
    # values: 0.71868417702905363
    # values: 1
    # values: 0.71489758861115449
    # values: 0.15289065587510078
    # values: 0.24954452327252891
    # values: 0.039841957551810879
    # values: 0.015352928689829664
    # values: 0.01756568152410479
    # values: 0.027205681597337543
    # }
    # correlations {
    # values: 0.88260056834116207
    # values: 0.7148975886111546
    # values: 1
    # values: 0.26974397819760371
    # values: 0.40833798755773076
    # values: 0.052872682257353996
    # values: 0.030250610606859983
    # values: 0.038242191424089876
    # values: 0.021726322573938063
    # }
    # correlations {
    # values: 0.23684883754736527
    # values: 0.15289065587510078
    # values: 0.26974397819760365
    # values: 0.99999999999999989
    # values: 0.58278525698102157
    # values: -0.0023992928238309088
    # values: 0.036767138937727227
    # values: -0.024029429775781139
    # values: 0.009064574908496284
    # }
    # correlations {
    # values: 0.3425406456087533
    # values: 0.24954452327252888
    # values: 0.40833798755773076
    # values: 0.58278525698102157
    # values: 1
    # values: 0.022351522227494688
    # values: 0.043057663404089876
    # values: 0.0020389651863856706
    # values: -0.002607106897262782
    # }
    # correlations {
    # values: 0.06382582934715679
    # values: 0.039841957551810879
    # values: 0.052872682257353996
    # values: -0.0023992928238309088
    # values: 0.022351522227494688
    # values: 1
    # values: 0.54855397217600743
    # values: 0.648919087494715
    # values: 0.19886393090334936
    # }
    # correlations {
    # values: 0.044086617067059207
    # values: 0.015352928689829662
    # values: 0.030250610606859983
    # values: 0.036767138937727234
    # values: 0.043057663404089876
    # values: 0.54855397217600743
    # values: 1
    # values: 0.38208102805903482
    # values: 0.33212789329062714
    # }
    # correlations {
    # values: 0.040928131400150572
    # values: 0.017565681524104787
    # values: 0.038242191424089869
    # values: -0.024029429775781139
    # values: 0.0020389651863856706
    # values: 0.648919087494715
    # values: 0.38208102805903482
    # values: 1
    # values: 0.056605322378432063
    # }
    # correlations {
    # values: 0.040303062059497748
    # values: 0.027205681597337543
    # values: 0.021726322573938063
    # values: 0.0090645749084962857
    # values: -0.002607106897262782
    # values: 0.19886393090334933
    # values: 0.33212789329062714
    # values: 0.056605322378432063
    # values: 1
    # }
    # time_grid: 0
    # time_grid: 0.94841269841269837
    # time_grid: 1.9841269841269842
    # time_grid: 3.0198412698412698
    # time_grid: 4.0515873015873014
    # time_grid: 5.2619047619047619


    # print("=============== PrcingInput =================")
    # print(input_data)

    assert input_data is not None 
    





test_financial_params()