import sys
import json
from datetime import datetime

def rebalance_portfolio(date, portfolio):
    # Ici, vous intégrerez votre code de hedging pour le rebalancement
    # Ceci est un exemple de retour
    result = {
        'rebalancing': [
            {
                'name': 'Eurostoxx50',
                'previousQuantity': '0.000000',
                'newQuantity': '0.08376319082136002'
            },
            {
                'name': 'HANGSENG',
                'previousQuantity': '0.000000',
                'newQuantity': '0.153208856188453'
            }
        ]
    }
    return result

if __name__ == "__main__":
    date = sys.argv[1]
    portfolio = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    result = rebalance_portfolio(date, portfolio)
    print(json.dumps(result))