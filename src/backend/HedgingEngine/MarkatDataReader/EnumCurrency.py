from enum import Enum
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex

class EnumCurrency(Enum):
    EUR = "EUR"
    USD = "USD"
    JPY = "JPY"
    GBP = "GBP"
    AUD = "AUD"

    def str_to_enum(name: str) -> EnumCurrency:
        """
        Converts a string to an EnumCurrency object.

        Args:
            str (str): The string to convert.

        Returns:
            EnumCurrency: The EnumCurrency object.
        """
        match name :
            case "EUR":
                return EnumCurrency.EUR
            case "USD":
                return EnumCurrency.USD
            case "JPY":
                return EnumCurrency.JPY
            case "GBP":
                return EnumCurrency.GBP
            case "AUD":
                return EnumCurrency.AUD
            case _:
                raise ValueError("Invalid currency")
            
