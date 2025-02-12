from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialParam.AssetDescription import AssetDescription
from backend.HedgingEngine.FinancialParam.FormuleDescription import FormuleDescription



class FinancialParam : 

    def __init__(self , dataReader : MarketDataReader  ):
        
        self.dataReader : MarketDataReader = dataReader
        self.assetDescription : AssetDescription
        self.formuleDescription : FormuleDescription


    
            