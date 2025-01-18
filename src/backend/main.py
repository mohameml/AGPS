from fastapi import FastAPI

# Création de l'application FastAPI
app = FastAPI()

# Route de base
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur FastAPI avec Uvicorn!"}


