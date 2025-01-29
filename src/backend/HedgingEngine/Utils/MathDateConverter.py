import numpy as np
from datetime import datetime

class MathDateConverter : 

    def __init__(self , workingDaysPerYear  : int):
        
        self.workingDaysPerYear = workingDaysPerYear
    
    def ConvertToMathDistance(self , date_from : datetime ,  date_until : datetime) -> float :

        if date_from < date_until :
            return float(np.busday_count(date_from.date(), date_until.date()) / self.workingDaysPerYear)
        else :  
            return float(np.busday_count(date_until.date(), date_from.date()) / self.workingDaysPerYear)
