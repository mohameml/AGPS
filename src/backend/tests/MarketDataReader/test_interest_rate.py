import pytest
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.InterestRate import InterestRate

def test_interest_rate_valid():
    """Teste la création d'un InterestRate valide."""
    interest_rate = InterestRate(currency=EnumCurrency.USD, rate=0.05)

    assert interest_rate.currency == EnumCurrency.USD
    assert interest_rate.rate == 0.05

def test_interest_rate_invalid_currency():
    """Teste si une erreur est levée pour une devise invalide."""
    with pytest.raises(ValueError, match="the type of currency must be a EnumCurrency"):
        InterestRate(currency="USD", rate=0.05)

def test_interest_rate_invalid_rate_type():
    """Teste si une erreur est levée pour un taux non numérique."""
    with pytest.raises(ValueError, match="rate must be a number"):
        InterestRate(currency=EnumCurrency.USD, rate="invalid")

def test_interest_rate_negative_rate():
    """Teste si un taux négatif est accepté (dépend du besoin métier)."""
    interest_rate = InterestRate(currency=EnumCurrency.USD, rate=-0.01)
    assert interest_rate.rate == -0.01  # Vérifie que la valeur est bien stockée

def test_interest_rate_display_info():
    """Teste l'affichage des informations."""
    interest_rate = InterestRate(currency=EnumCurrency.EUR, rate=0.03)
    
    output = interest_rate.display_info()
    assert output == "Currency: EUR, Interest Rate: 3.00%"
