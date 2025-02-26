import sys
import os
import json

from backend.HedgingEngine.MarkatDataReader.MarketDataReader import MarketDataReader
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.Hedging.Hedger import Hedger 

def main():
    # Vérification des arguments
    if len(sys.argv) != 4:
        print(f"Erreur : Taille attendue des arguments est 3, alors que la taille est {len(sys.argv) - 1}")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
        print("Chemin non valide passé en arguments")
        sys.exit(1)

    if not (sys.argv[1].endswith(".json") and sys.argv[2].endswith(".csv") and sys.argv[3].endswith(".json")):
        print("Les extensions de fichiers attendues sont : .json, .csv et .json")
        sys.exit(1)

    # Lecture des données de marché
    # data = MarketDataReader.read_data_feeds(sys.argv[2])
    
    # # Lecture des paramètres financiers
    # with open(sys.argv[1], 'r') as file:
    #     json_string = file.read()
    # financial_param = JsonIO.from_json(json_string)
    
    # # Exécution du hedging
    # hedger = Hedging(financial_param)
    # list_output = hedger.hedge(data)
    
    # # Sauvegarde des résultats
    # with open(sys.argv[3], 'w') as file:
    #     json.dump(JsonIO.to_json(list_output), file)

if __name__ == "__main__":
    main()
