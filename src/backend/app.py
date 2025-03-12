from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import Dict
from backend.HedgingEngine.Hedging.Hedger import Hedging
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
import os 
import pandas as pd 
from backend.HedgingEngine.MarkatDataReader.MarketDataReader import EnumIndex


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "../../data/DonneesGPS2025.xlsx")
FILE_PATH = os.path.abspath(FILE_PATH)


indexes = [
    EnumIndex.ASX200 , 
    EnumIndex.EUROSTOXX50 ,
    EnumIndex.FTSE100 ,
    EnumIndex.SP500 ,
    EnumIndex.TOPIX
]

dates_cibles = [
    pd.to_datetime('01-04-2010', format="%d-%m-%Y"),
    pd.to_datetime('01-04-2011', format="%d-%m-%Y"),
    pd.to_datetime('01-04-2012', format="%d-%m-%Y"),
    pd.to_datetime('01-04-2013', format="%d-%m-%Y"),
]

T0 = pd.to_datetime('01-05-2009' , format='%d-%m-%Y')
T = pd.to_datetime('01-06-2010', format='%d-%m-%Y')

# Exemple de modèle Pydantic pour la requête POST
class PortfolioDataRequest(BaseModel):
    cash: float
    compos: Dict[str, float]
    date: datetime
    isFirstTime: bool

# Créer une instance de HedgeEngine
financial_params = FinancialParams()
hedge_engine = HedgeEngine()


# Création de l'application FastAPI
app = FastAPI()


# Route de base
@app.get("/")
def read_root():
    message =  {"message": "Bienvenue sur FastAPI avec Uvicorn!"}
    return message




# Endpoint GET pour récupérer des paramètres à partir de l'URL
@app.get("/hedge/{rebalancingDate}")
async def get_hedge_params(rebalancingDate: datetime):
    try:
        return {"message": f"Rebalancing Date: {rebalancingDate}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint POST pour recevoir les données de type PortfolioData et lancer la méthode hedge
@app.post("/hedge")
async def post_hedge(portfolio_data: PortfolioDataRequest):
    try:
        # Créer une instance de PortfolioData avec les données reçues
        portfolio_data_instance = PortfolioData(
            cash=portfolio_data.cash,
            compos=portfolio_data.compos,
            date=portfolio_data.date,
            isFirstTime=portfolio_data.isFirstTime
        )

        # Appeler la méthode hedge avec les données fournies
        history_data = ListDataFeed(data=[])  # Exemple d'historique de données vide
        result = hedge_engine.hedge(historyData=history_data, rebalancingDate=portfolio_data.date, portfolioData=portfolio_data_instance)

        # Retourner le résultat sous forme de JSON
        return JSONResponse(content={
            "result": result.result,
            "details": result.details
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
