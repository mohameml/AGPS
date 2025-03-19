import pytest
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.ExchangeRate import ExchangeRate
from backend.HedgingEngine.MarkatDataReader.ExchangeRateList import ExchangeRateList

def test_exchange_rate_list_add():
    """Teste l'ajout d'un ExchangeRate à la liste."""
    rate_list = ExchangeRateList()
    rate = ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR)
    
    rate_list.add(rate)
    
    assert len(rate_list) == 1
    assert rate_list.get(0) == rate

def test_exchange_rate_list_get():
    """Teste la récupération d'un élément par son index."""
    rate_list = ExchangeRateList()
    rate1 = ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR)
    rate2 = ExchangeRate(base_currency=EnumCurrency.GBP, rate=0.85, target_currency=EnumCurrency.EUR)

    rate_list.add(rate1)
    rate_list.add(rate2)

    assert rate_list.get(0) == rate1
    assert rate_list.get(1) == rate2

def test_exchange_rate_list_get_all():
    """Teste la récupération de tous les éléments."""
    rate_list = ExchangeRateList()
    rates = [
        ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR),
        ExchangeRate(base_currency=EnumCurrency.GBP, rate=0.85, target_currency=EnumCurrency.EUR)
    ]

    for rate in rates:
        rate_list.add(rate)

    assert rate_list.get_all() == rates

def test_exchange_rate_list_length():
    """Teste la taille de la liste après plusieurs ajouts."""
    rate_list = ExchangeRateList()
    
    assert len(rate_list) == 0  # Liste vide

    rate_list.add(ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR))
    assert len(rate_list) == 1

    rate_list.add(ExchangeRate(base_currency=EnumCurrency.GBP, rate=0.85, target_currency=EnumCurrency.EUR))
    assert len(rate_list) == 2

def test_exchange_rate_list_str():
    """Teste la représentation en chaîne de caractères de la liste."""
    rate_list = ExchangeRateList()
    rate1 = ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR)
    rate2 = ExchangeRate(base_currency=EnumCurrency.GBP, rate=0.85, target_currency=EnumCurrency.EUR)

    rate_list.add(rate1)
    rate_list.add(rate2)

    assert str(rate_list) == str([rate1, rate2])

def test_exchange_rate_list_display_info(capfd):
    """Teste la méthode display_info()."""
    rate_list = ExchangeRateList()
    rate_list.display_info()
    captured = capfd.readouterr()
    assert captured.out.strip() == "No Data available."

    rate1 = ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR)
    rate_list.add(rate1)
    
    rate_list.display_info()
    captured = capfd.readouterr()
    assert "Exchange Rate: 1 USD = 1.1200 EUR" in captured.out.strip()
