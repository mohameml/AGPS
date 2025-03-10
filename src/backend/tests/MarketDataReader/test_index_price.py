import pytest
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.IndexPrice import IndexPrice

def test_index_price_valid():
    """Teste la création d'un IndexPrice valide."""
    index_price = IndexPrice(index_name=EnumIndex.SP500, currency=EnumCurrency.USD, price=4500.75)

    assert index_price.index_name == EnumIndex.SP500
    assert index_price.currency == EnumCurrency.USD
    assert index_price.price == 4500.75

def test_index_price_invalid_index():
    """Teste si une erreur est levée pour un index invalide."""
    with pytest.raises(ValueError, match="index_name doit être une instance de EnumIndex"):
        IndexPrice(index_name="SP500", currency=EnumCurrency.USD, price=4500.75)

def test_index_price_invalid_currency():
    """Teste si une erreur est levée pour une devise invalide."""
    with pytest.raises(ValueError, match="currency doit être une instance de EnumCurrency"):
        IndexPrice(index_name=EnumIndex.SP500, currency="USD", price=4500.75)

def test_index_price_invalid_price_type():
    """Teste si une erreur est levée pour un prix non numérique."""
    with pytest.raises(ValueError, match="price doit être un nombre"):
        IndexPrice(index_name=EnumIndex.SP500, currency=EnumCurrency.USD, price="invalid")

def test_index_price_negative_price():
    """Teste si une erreur est levée pour un prix négatif."""
    with pytest.raises(ValueError, match="price doit être un nombre positif"):
        IndexPrice(index_name=EnumIndex.SP500, currency=EnumCurrency.USD, price=-1000)

def test_index_price_display_info(capfd):
    """Teste l'affichage des informations."""
    index_price = IndexPrice(index_name=EnumIndex.SP500, currency=EnumCurrency.USD, price=4500.75)
    
    output = index_price.display_info()
    assert output == "Indice: SP500, Devise: USD, Prix: 4500.75"
