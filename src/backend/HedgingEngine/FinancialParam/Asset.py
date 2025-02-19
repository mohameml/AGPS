from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex


class  Asset :

    def __init__(self  , id : EnumIndex , volatility : float):
        
        self.id = id 
        self.volatility = volatility


    def display_info(self):

        print(f"Asset : id = {self.id.name} , volatility = {self.volatility}")
    
    