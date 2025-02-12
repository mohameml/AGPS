import sys
import json
from datetime import datetime

def get_stats(date):
    # Ici, vous intégrerez votre code de hedging pour les statistiques
    # Ceci est un exemple de retour
    stats = {
        'pnl': -8.451,
        'portfolioValue': 1104.287,
        'liquidativeValue': 1206.225,
        'flows': [
            {'date': '2009-01-05', 'value': 1000},
            {'date': '2010-01-04', 'value': -20},
            {'date': '2011-01-04', 'value': -30},
            {'date': '2012-01-04', 'value': -25},
            {'date': '2013-01-04', 'value': -20}
        ]
    }
    return stats

if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime('%Y-%m-%d')
    result = get_stats(date)
    print(json.dumps(result))