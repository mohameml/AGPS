from dataclasses import dataclass, field
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency

@dataclass
class ExchangeRate:
    """
    - Represents an exchange rate between two currencies.

    - Attributes:
        - base_currency (EnumCurrency): The base currency (e.g., USD, GBP).
        - target_currency (EnumCurrency): The target currency, default is EUR.
        - rate (float): The exchange rate value (e.g., 1.12 for USD/EUR).
    """
    base_currency: EnumCurrency
    target_currency: EnumCurrency = field(default=EnumCurrency.EUR)
    rate: float

    def __post_init__(self):
        """
        Validates the attributes after the initialization of the ExchangeRate object.
        """
        if not isinstance(self.base_currency, EnumCurrency):
            raise ValueError(f"base_currency must be an instance of EnumCurrency, got {type(self.base_currency)}.")

        if not isinstance(self.target_currency, EnumCurrency):
            raise ValueError(f"target_currency must be an instance of EnumCurrency, got {type(self.target_currency)}.")

        if self.base_currency == self.target_currency:
            raise ValueError("base_currency and target_currency cannot be the same.")

        if not isinstance(self.rate, (int, float)):
            raise ValueError("rate must be a numeric value.")



    def display_info(self) -> str:
        """
        Returns a formatted string with exchange rate details.

        Returns:
            str: A formatted string showing exchange rate details.
        """
        return f"Exchange Rate: 1 {self.base_currency.name} = {self.rate:.4f} {self.target_currency.name}"
