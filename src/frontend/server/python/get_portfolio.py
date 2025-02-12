import sys
import json
from datetime import datetime

def get_portfolio(date):
    # Ici, vous intégrerez votre code de hedging
    # Ceci est un exemple de retour
    portfolio = {
        'data': [
            {
                'name': 'REUR',
                'quantity': '1000.000000',
                'price': '0.028300',
                'foreignPrice': '0.028300',
                'total': '1000.000000'
            },
            {
                'name': 'RUSD',
                'quantity': '0.000000',
                'price': '0.010879',
                'foreignPrice': '0.014800',
                'total': '0.000000'
            }
        ]
    }
    return portfolio

if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime('%Y-%m-%d')
    result = get_portfolio(date)
    print(json.dumps(result))