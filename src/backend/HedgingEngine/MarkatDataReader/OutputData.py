from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class OutputData:
    date: datetime
    value: float
    deltas: List[float]
    deltas_std_dev: List[float]
    price: List[float]
    price_std_dev: List[float]

    def __post_init__(self):
        """Validation et conversion des données après l'initialisation."""
        # Validation de 'date'
        if not isinstance(self.date, datetime):
            raise TypeError("L'attribut 'date' doit être un objet datetime.")

        # Conversion de 'value' en float
        self.value = float(self.value)

        # Conversion des listes en listes de floats
        self.deltas = [float(x) for x in self.deltas]
        self.deltas_std_dev = [float(x) for x in self.deltas_std_dev]
        self.price = [float(x) for x in self.price]
        self.price_std_dev = [float(x) for x in self.price_std_dev]