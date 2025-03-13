from datetime import datetime
from pydantic import BaseModel

class NextDayRequest(BaseModel):
    date : datetime
