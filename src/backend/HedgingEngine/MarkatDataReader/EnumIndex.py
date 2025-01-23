from enum import Enum
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import  EnumCurrency

class EnumIndex(Enum):
    ASX200 = "ASX200"
    EUROSTOXX50 = "EUROSTOXX50"
    FTSE100 = "FTSE100"
    SP500 = "SP500"
    TOPIX = "TOPIX"


    def str_to_enum(name: str) -> EnumIndex:
        """
        Converts a string to an EnumIndex object.

        Args:
            str (str): The string to convert.

        Returns:
            EnumIndex: The EnumIndex object.
        """
        match name :
            case "SP500":
                return EnumIndex.SP500
            case "CAC40":
                return EnumIndex.CAC40
            case "DAX":
                return EnumIndex.DAX
            case "NIKKEI":
                return EnumIndex.NIKKEI
            case "FTSE100":
                return EnumIndex.FTSE100
            case "TOPIX":
                return EnumIndex.TOPIX
            case _:
                raise ValueError("Invalid index")



# Dictionnaire d'association entre les index et les devises
index_to_currency = {
    EnumIndex.ASX200: EnumCurrency.AUD,
    EnumIndex.EUROSTOXX50: EnumCurrency.EUR,
    EnumIndex.FTSE100: EnumCurrency.GBP,
    EnumIndex.SP500: EnumCurrency.USD,
    EnumIndex.TOPIX: EnumCurrency.JPY
}

