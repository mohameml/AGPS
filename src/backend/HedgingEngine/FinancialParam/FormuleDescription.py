from datetime import datetime
from typing import List
from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter

class FormuleDescription : 

    def __init__(self , t0 : datetime , list_ti : List[datetime] , T : datetime , nombreOfDaysInOneYear : int):

        self.creationDate = t0 
        self.converter = MathDateConverter(nombreOfDaysInOneYear)
        self.paymentDates = list_ti  # t1 , t2 , t3 , t4
        self.maturity = T 
        self.time_grid_datetime = [t0] + list_ti + [T] 
        
        self.time_grid = [] 
        nbDays = len(self.paymentDates) + 2 
        
        for i in range(nbDays) : 
            self.time_grid.append(self.converter.ConvertToMathDistance(t0 , self.time_grid_datetime[i]))

        # self.dividendes = []
        # self.V0 = V0 


