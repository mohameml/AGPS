import pytest 

from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency




def test_str_to_enum_currency():

    assert EnumCurrency.str_to_enum("AUD") == EnumCurrency.AUD
    assert EnumCurrency.str_to_enum("EUR") == EnumCurrency.EUR
    assert EnumCurrency.str_to_enum("GBP") == EnumCurrency.GBP
    assert EnumCurrency.str_to_enum("USD") == EnumCurrency.USD
    assert EnumCurrency.str_to_enum("JPY") == EnumCurrency.JPY

    with pytest.raises(ValueError, match=f"Invalid currency"):
        EnumCurrency.str_to_enum("Hello")




