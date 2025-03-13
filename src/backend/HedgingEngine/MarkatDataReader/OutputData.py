from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class OutputData:
    date: datetime
    value: float
    deltas: List[float]
    deltas_std_dev: List[float]
    price: float
    price_std_dev: float


    