from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class PortfolioData :
    cash : float 
    compos : Dict[str , float]
    date : datetime
    isFirstTime : bool