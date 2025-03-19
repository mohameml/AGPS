import pytest
from unittest.mock import MagicMock
import numpy as np
from backend.HedgingEngine.FinancialEstimator.VolatilityEstimator import VolatilityEstimator
from backend.HedgingEngine.FinancialEstimator.CorrelationMatrixEstimator import CorrelationMatrixEstimator
from backend.HedgingEngine.FinancialEstimator.RiskFreeRateEstimator import RiskFreeRateEstimator
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator

@pytest.fixture
def mock_market_data_reader():
    # Mock the MarketDataReader object
    market_data_reader = MagicMock(MarketDataReader)

    # Mocking attributes in MarketDataReader
    market_data_reader._interest_rate_history = MagicMock()
    market_data_reader._exchange_rate_history = MagicMock()
    market_data_reader._index_price_history = MagicMock()

    # Mocking methods in MarketDataReader
    market_data_reader._interest_rate_history.get_all_rate_by_curr_name = MagicMock(return_value=[0.01, 0.02, 0.015])
    market_data_reader._exchange_rate_history.get_all_rate_by_currency_name = MagicMock(return_value=[1.1, 1.2, 1.3])
    market_data_reader._index_price_history.get_all_price_by_index_name = MagicMock(return_value=[100, 102, 105])
    market_data_reader._index_price_history.get_all_price_for_all_index_name = MagicMock(return_value=[[100, 102, 105], [200, 202, 205]])
    market_data_reader._exchange_rate_history.get_all_rate_for_all_curr_name = MagicMock(return_value=[[1.1, 1.2, 1.3], [1.3, 1.4, 1.5], [1.5, 1.6, 1.7]])

    return market_data_reader

@pytest.fixture
def financial_estimator(mock_market_data_reader):
    return FinancialEstimator(mock_market_data_reader)

def test_estimate_dict_interest_rate(financial_estimator, mock_market_data_reader):
    # Test the estimate_dict_interest_rate method
    dict_interest_rate = financial_estimator.estimate_dict_interest_rate()

    # Verifying that the method returns the correct interest rate for each currency
    assert EnumCurrency.USD in dict_interest_rate
    assert dict_interest_rate[EnumCurrency.USD] == 0.015  # Expected average value from the mocked rates

    assert EnumCurrency.EUR in dict_interest_rate
    assert dict_interest_rate[EnumCurrency.EUR] == 0.015  # Expected average value

def test_estimate_dict_volatility_exchange_rate(financial_estimator, mock_market_data_reader):
    # Test the estimate_dict_volatility_exchange_rate method
    dict_volatility = financial_estimator.estimate_dict_volatility_exchange_rate()

    # Verifying that EUR has a volatility of 0.0
    assert dict_volatility[EnumCurrency.EUR] == 0.0

    # Verifying that other currencies have volatility calculated
    assert EnumCurrency.USD in dict_volatility

    assert np.allclose(dict_volatility[EnumCurrency.USD], 0.05 , atol=10e-2)  # Mocked volatility value

def test_estimate_dict_volatility_price(financial_estimator, mock_market_data_reader):
    # Test the estimate_dict_volatility_price method
    dict_volatility = financial_estimator.estimate_dict_volatility_price()

    # Verifying that volatilities for indices are calculated
    assert EnumIndex.SP500 in dict_volatility
    
    assert np.allclose(dict_volatility[EnumIndex.SP500], 0.07, atol=10e-2)


def test_estimate_matrix_corr(financial_estimator, mock_market_data_reader):
    # Test the estimate_matrix_corr method
    matrix_corr = financial_estimator.estimate_matrix_corr()

    # Verifying that the correlation matrix is not empty
    assert matrix_corr is not None
    assert matrix_corr.shape[0] == 5  # The number of rows should be the sum of index and exchange rate data


