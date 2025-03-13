import numpy as np
from datetime import datetime

class MathDateConverter : 

    def __init__(self , workingDaysPerYear  : int , T0 : datetime):
        self.workingDaysPerYear = workingDaysPerYear
        self.T0 = T0 

        
    def ConvertToMathDistance(self, date_until : datetime ,  date_from : datetime = None) -> float :

        if date_from is None :
            date_from = self.T0

        if date_from < date_until :
            return float(np.busday_count(date_from.date(), date_until.date()) / self.workingDaysPerYear)
        else :  
            return float(np.busday_count(date_until.date(), date_from.date()) / self.workingDaysPerYear)
