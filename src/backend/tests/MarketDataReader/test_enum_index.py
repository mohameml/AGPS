import pytest 

from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumIndex import index_to_currency



def test_str_to_enum_index():

    assert EnumIndex.str_to_enum("ASX200") == EnumIndex.ASX200
    assert EnumIndex.str_to_enum("EUROSTOXX50") == EnumIndex.EUROSTOXX50
    assert EnumIndex.str_to_enum("FTSE100") == EnumIndex.FTSE100
    assert EnumIndex.str_to_enum("SP500") == EnumIndex.SP500
    assert EnumIndex.str_to_enum("TOPIX") == EnumIndex.TOPIX

    name : str = "Hello"
    with pytest.raises(ValueError, match=f"Invalid index : {name}"):
        EnumIndex.str_to_enum(name)



def test_enum_index_to_curr():
    
    assert index_to_currency[EnumIndex.ASX200] == EnumCurrency.AUD
    assert index_to_currency[EnumIndex.EUROSTOXX50] == EnumCurrency.EUR
    assert index_to_currency[EnumIndex.FTSE100] == EnumCurrency.GBP
    assert index_to_currency[EnumIndex.SP500] == EnumCurrency.USD
    assert index_to_currency[EnumIndex.TOPIX] == EnumCurrency.JPY
