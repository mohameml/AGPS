from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialParam.AssetDescription import AssetDescription
from backend.HedgingEngine.FinancialParam.FormuleDescription import FormuleDescription
from typing import List
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from datetime import datetime 
import json



# TODO : passer MarketDataReader comme args au lieur de file_path 

class FinancialParams : 

    def __init__(self , file_path: str, indexes: List[EnumIndex], T0: datetime, T: datetime , list_ti : List[datetime] ):
        
        self.nombreOfDaysInOneYear = 252 

        self.marketDataReader : MarketDataReader = MarketDataReader(file_path , indexes , T0 , T)

        self.assetDescription : AssetDescription = AssetDescription()
        self.assetDescription.estimate_params(self.marketDataReader)
        
        self.formuleDescription : FormuleDescription = FormuleDescription(T0 , list_ti , T , self.nombreOfDaysInOneYear)

    def to_json(self, json_path: str):
        """Sauvegarde certains attributs de l'objet dans un fichier JSON."""
        data = {
            "nombreOfDaysInOneYear": self.nombreOfDaysInOneYear,
            "assetDescription": self._serialize_asset_description(),
            "formuleDescription": self._serialize_formule_description()
        }

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, default=str)  # `default=str` pour gérer datetime

    def _serialize_asset_description(self):
        """Convertit l'objet `assetDescription` en dictionnaire sérialisable."""
        return {
            "domesticCurrencyId": self.assetDescription.domesticCurrencyId,
            "matrix_corr": self.assetDescription.matrix_corr.tolist(),  # Convertir NumPy array en liste
            "assets": [{"id": asset.id.name, "volatility": asset.volatility} for asset in self.assetDescription.assets],
            "currencies": [
                {"id": currency.id.name, "volatility": currency.volatility, "rate": currency.rate}
                for currency in self.assetDescription.currencies
            ],
        }

    def _serialize_formule_description(self):
        """Convertit l'objet `formuleDescription` en dictionnaire sérialisable."""
        return {
            "creationDate": self.formuleDescription.creationDate.isoformat(),
            "paymentDates": [date.isoformat() for date in self.formuleDescription.paymentDates],
            "maturity": self.formuleDescription.maturity.isoformat(),
            "time_grid": [date.isoformat() for date in self.formuleDescription.time_grid],
        }
