import pytest
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.ExchangeRate import ExchangeRate

def test_exchange_rate_valid():
    """Teste la création d'un objet ExchangeRate valide."""
    rate = ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR)
    assert rate.base_currency == EnumCurrency.USD
    assert rate.target_currency == EnumCurrency.EUR
    assert rate.rate == 1.12

def test_exchange_rate_default_target_currency():
    """Teste que la devise cible par défaut est bien EUR."""
    rate = ExchangeRate(base_currency=EnumCurrency.GBP, rate=0.85)
    assert rate.target_currency == EnumCurrency.EUR

def test_exchange_rate_invalid_base_currency():
    """Teste si une erreur est levée si base_currency n'est pas un EnumCurrency."""
    with pytest.raises(ValueError, match="base_currency must be an instance of EnumCurrency"):
        ExchangeRate(base_currency="USD", rate=1.12)

def test_exchange_rate_invalid_target_currency():
    """Teste si une erreur est levée si target_currency n'est pas un EnumCurrency."""
    with pytest.raises(ValueError, match="target_currency must be an instance of EnumCurrency"):
        ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency="EUR")

def test_exchange_rate_same_currencies():
    """Teste si une erreur est levée si base_currency et target_currency sont identiques."""
    with pytest.raises(ValueError, match="base_currency and target_currency cannot be the same"):
        ExchangeRate(base_currency=EnumCurrency.USD, rate=1.0, target_currency=EnumCurrency.USD)

def test_exchange_rate_invalid_rate():
    """Teste si une erreur est levée si rate n'est pas un nombre."""
    with pytest.raises(ValueError, match="rate must be a numeric value"):
        ExchangeRate(base_currency=EnumCurrency.USD, rate="invalid_rate")

def test_display_info():
    """Teste la méthode display_info()."""
    rate = ExchangeRate(base_currency=EnumCurrency.USD, rate=1.12, target_currency=EnumCurrency.EUR)
    assert rate.display_info() == "Exchange Rate: 1 USD = 1.1200 EUR"
