from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from dataclasses import dataclass



@dataclass
class InterestRate:
    """
    Represents an interest rate for a specific currency.

    Attributes:
        currency (str): The currency associated with the interest rate (e.g., USD, EUR).
        rate (float): The interest rate value (e.g., 0.05 for 5%).
    """
    currency: EnumCurrency
    rate: float

    def __post_init__(self):
        """Validates the data after initialization."""

        if not isinstance(self.currency, EnumCurrency) :
            raise ValueError("the type of currency must be a EnumCurrency.")
        
        if not isinstance(self.rate, (int, float)):
            raise ValueError("rate must be a number.")


    def display_info(self) -> str:
        """
        Returns a formatted string with the currency and interest rate.

        Returns:
            str: The formatted string.
        """
        return f"Currency: {self.currency.value}, Interest Rate: {self.rate * 100:.2f}%"




