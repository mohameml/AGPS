from enum import Enum
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import  EnumCurrency


class EnumIndex(Enum):
    EUROSTOXX50 = "EUROSTOXX50"
    SP500 = "SP500"
    FTSE100 = "FTSE100"
    TOPIX = "TOPIX"
    ASX200 = "ASX200"
    # NIKKEI='NIKKEI'
    TOPIX = "TOPIX"
    ASX200 = "ASX200"
    # NIKKEI='NIKKEI'

    def str_to_enum(name: str) :
        """
        Converts a string to an EnumIndex object.

        Args:
            str (str): The string to convert.

        Returns:
            EnumIndex: The EnumIndex object.
        """
        match name :
            case "ASX200":
                return EnumIndex.ASX200
            case "ASX200":
                return EnumIndex.ASX200
            case "EUROSTOXX50":
                return EnumIndex.EUROSTOXX50
            case "FTSE100":
                return EnumIndex.FTSE100
            case "SP500":
                return EnumIndex.SP500
            case "TOPIX":
                return EnumIndex.TOPIX
            case "TOPIX":
                return EnumIndex.TOPIX

            # case "NIKKEI":
            #     return EnumIndex.NIKKEI
            # case "NIKKEI":
            #     return EnumIndex.NIKKEI
            
            case _:
                raise ValueError(f"Invalid index : {name}")



# Dictionnaire d'association entre les index et les devises
index_to_currency = {
    EnumIndex.EUROSTOXX50: EnumCurrency.EUR,
    EnumIndex.SP500: EnumCurrency.USD,
    EnumIndex.FTSE100: EnumCurrency.GBP,
    EnumIndex.TOPIX: EnumCurrency.JPY,
    EnumIndex.ASX200: EnumCurrency.AUD,
    # EnumIndex.NIKKEI: EnumCurrency.JPY,
    # EnumIndex.FTSE100: EnumCurrency.GBP
    EnumIndex.TOPIX: EnumCurrency.JPY,
    EnumIndex.ASX200: EnumCurrency.AUD,
    # EnumIndex.NIKKEI: EnumCurrency.JPY,
    # EnumIndex.FTSE100: EnumCurrency.GBP
}