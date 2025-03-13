from fastapi import FastAPI

from backend.API.controllers import market_controller
from backend.API.controllers import hedge_controller


# =============== app ===============
app = FastAPI()

# ================ routes ================
app.include_router(market_controller.router)
app.include_router(hedge_controller.router)

# Route de base
@app.get("/")
def hello():
    message =  {"message": "Bienvenue sur API AGPS Equipe 6, tester les routes /next-day et /hedge"}
    return message










