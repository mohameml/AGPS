from datetime import datetime
from typing import List
from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter

class TimeGrid : 

    def __init__(self , T0 : datetime , list_ti : List[datetime] , T : datetime ) :

        self.creationDate = T0 
        self.paymentDates = list_ti 
        self.maturity = T 
        self.time_grid_datetime = [T0] + list_ti + [T] 
        
    def get_time_grid(self , converter : MathDateConverter) -> List[float] :
        time_grid = [converter.ConvertToMathDistance(date) for date in self.time_grid_datetime] 
        return time_grid
