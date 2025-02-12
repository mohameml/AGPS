from datetime import datetime
from typing import List

class FormuleDescription : 

    def __init__(self , t0 : datetime , list_ti : List[datetime] , T : datetime):

        self.creationDate = t0 
        self.paymentDates = list_ti  # t1 , t2 , t3 , t4
        self.maturity = T 
        self.time_grid = [t0] + list_ti + [T]
        # self.dividendes = []
        # self.V0 = V0 


