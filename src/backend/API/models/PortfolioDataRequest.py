from pydantic import BaseModel
from typing import Dict
from datetime import datetime

class PortfolioDataRequest(BaseModel):
    cash: float
    compos: Dict[str, float]
    date: datetime
    isFirstTime: bool
    currDate : datetime