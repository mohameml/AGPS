from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency


class  Currency :

    def __init__(self  , id : EnumCurrency , volatility : float , rate : float):
        
        self.id = id 
        self.volatility = volatility
        self.rate = rate 


    def display_info(self):

        print(f"Currency : id = {self.id.name} , volatility = {self.volatility} , rate = {self.rate}")
    