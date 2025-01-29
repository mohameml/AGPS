from backend.HedgingEngine.MarkatDataReader.DataFeed import DataFeed
from datetime import datetime

# Exemple d'utilisation
if __name__ == "__main__":
    # Initialisation de la classe avec des données d'exemple
    data_feed = DataFeed(
        date=datetime(2025, 1, 29),
        index_price={'SP500': 4000.5, 'NASDAQ': 12000.0},
        inert_state_rate={'SP500': 0.02, 'NASDAQ': 0.015},
        exchanges={'NYSE': 'New York Stock Exchange', 'NASDAQ': 'NASDAQ Stock Market'}
    )
    
    # Affichage de l'objet
    print(data_feed)

    # Ajout de nouvelles données
    data_feed.add_index_price('DOWJONES', 33000.0)
    data_feed.add_inert_state_rate('DOWJONES', 0.018)
    data_feed.add_exchange('LSE', 'London Stock Exchange')

    # Affichage mis à jour
    print("\nAprès ajout des données supplémentaires:")
    print(data_feed)

    # Accès aux informations
    print("\nPrix de l'indice NASDAQ :", data_feed.get_index_price('NASDAQ'))
    print("Taux d'état inertiel pour le SP500 :", data_feed.get_inert_state_rate('SP500'))
    print("Informations sur l'échange LSE :", data_feed.get_exchange_info('LSE'))
