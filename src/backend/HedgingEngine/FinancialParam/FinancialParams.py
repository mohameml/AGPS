from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialParam.AssetDescription import AssetDescription
from backend.HedgingEngine.FinancialParam.TimeGrid import TimeGrid
from typing import List
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.FinancialEstimator.FinancialEstimator import FinancialEstimator
from datetime import datetime 
import json




class FinancialParams : 

    def __init__(self , financialEstimator : FinancialEstimator, T0: datetime, T: datetime , list_ti : List[datetime] ):
        
        self.nombreOfDaysInOneYear = 252 

        self.marketDataReader = financialEstimator.marketDataReader

        self.assetDescription : AssetDescription = AssetDescription(financialEstimator)
        
        self.time_grid : TimeGrid = TimeGrid(T0 , list_ti , T)


    def set_nb_days_in_one_year(self , year : int):
        self.nombreOfDaysInOneYear = self.marketDataReader.get_nb_days_in_one_year(year)

    def to_object(self):
        """Convertit l'objet en dictionnaire."""
        return {
            "nombreOfDaysInOneYear": self.nombreOfDaysInOneYear,
            "assetDescription": self._serialize_asset_description(),
            "TimeGrid": self._serialize_formule_description()
        }

    def to_json(self, json_path: str):
        """Sauvegarde certains attributs de l'objet dans un fichier JSON."""
        data = {
            "nombreOfDaysInOneYear": self.nombreOfDaysInOneYear,
            "assetDescription": self._serialize_asset_description(),
            "TimeGrid": self._serialize_formule_description()
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
        """Convertit l'objet `TimeGrid` en dictionnaire sérialisable."""
        return {
            "creationDate": self.time_grid.creationDate.isoformat(),
            "paymentDates": [date.isoformat() for date in self.time_grid.paymentDates],
            "maturity": self.time_grid.maturity.isoformat(),
        }
