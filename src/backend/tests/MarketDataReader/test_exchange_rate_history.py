import pytest
from datetime import datetime
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.ExchangeRate import ExchangeRate
from backend.HedgingEngine.MarkatDataReader.ExchangeRateList import ExchangeRateList
from backend.HedgingEngine.MarkatDataReader.ExchangeRateHistory import ExchangeRateHistory

def test_exchange_rate_history_add_and_get():
    """Teste l'ajout et la récupération d'un enregistrement."""
    history = ExchangeRateHistory()
    date = datetime(2024, 1, 1)

    rate_list = ExchangeRateList()
    rate_list.add(ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR))

    history.add_record(date, rate_list)
    retrieved_list = history.get_record(date)

    assert retrieved_list == rate_list
    assert len(retrieved_list) == 1
    assert retrieved_list.get(0).base_currency == EnumCurrency.USD

def test_exchange_rate_history_get_invalid_date():
    """Teste si une erreur est levée lorsqu'on essaie de récupérer une date inexistante."""
    history = ExchangeRateHistory()
    date = datetime(2024, 1, 1)

    with pytest.raises(KeyError, match=f"No record found for date: {date}"):
        history.get_record(date)

def test_exchange_rate_history_list_dates():
    """Teste la liste des dates stockées."""
    history = ExchangeRateHistory()
    dates = [datetime(2024, 1, 1), datetime(2024, 1, 2)]

    for date in dates:
        history.add_record(date, ExchangeRateList())

    stored_dates = history.list_dates()
    assert set(stored_dates) == set(dates)

def test_exchange_rate_history_display_info(capfd):
    """Teste la méthode display_info()."""
    history = ExchangeRateHistory()
    
    # Cas où il n'y a pas de données
    history.display_info()
    captured = capfd.readouterr()
    assert captured.out.strip() == "No historical data available."

    # Cas avec des données
    date = datetime(2024, 1, 1)
    rate_list = ExchangeRateList()
    rate_list.add(ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR))
    
    history.add_record(date, rate_list)
    history.display_info()
    
    captured = capfd.readouterr()
    assert "Date: 2024-01-01" in captured.out
    assert "Exchange Rate: 1 USD = 1.1200 EUR" in captured.out
