from dataclasses import dataclass

from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency


@dataclass
class IndexPrice:
    """
    - Représente le prix d'un indice de marché dans une devise spécifique.

    - Attributes:
        - index_name (str): Nom de l'indice (ex: SP500, CAC40, etc.).
        - currency (str): Devise associée à l'indice (ex: USD, EUR).
        - price (float): Valeur du prix de l'indice.
    """
    index_name: EnumIndex
    currency: EnumCurrency
    price: float

    def __post_init__(self):
        """
        Validation après l'initialisation de l'objet IndexPrice.
        """
        if not isinstance(self.index_name, EnumIndex):
            raise ValueError(f"index_name doit être une instance de EnumIndex, mais {type(self.index_name)} trouvé.")
        
        if not isinstance(self.currency, EnumCurrency):
            raise ValueError(f"currency doit être une instance de EnumCurrency, mais {type(self.currency)} trouvé.")
        
        if not isinstance(self.price, (int, float)):
            raise ValueError("price doit être un nombre.")
        
        if self.price < 0:
            raise ValueError("price doit être un nombre positif.")



    def display_info(self) -> str:
        return f"Indice: {self.index_name.value}, Devise: {self.currency.value}, Prix: {self.price:.2f}"


