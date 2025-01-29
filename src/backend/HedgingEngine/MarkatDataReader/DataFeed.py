from datetime import datetime
from typing import Dict

class DataFeed:
    def __init__(self, date: datetime, 
                index_price: Dict[str, float], 
                intersate_rate: Dict[str, float], 
                exchanges: Dict[str, str]
        ):
        self.date = date
        self.index_price = index_price
        self.inert_state_rate = intersate_rate
        self.exchanges = exchanges

    
    def add_index_price(self, symbol: str, price: float):
        
        self.index_price[symbol] = price
    
    def add_inert_state_rate(self, symbol: str, rate: float):
        """
        Ajouter ou mettre à jour un taux d'état inertiel dans le dictionnaire `inert_state_rate`.
        
        :param symbol: Symbole associé au taux d'état inertiel
        :param rate: Valeur du taux d'état inertiel
        """
        self.inert_state_rate[symbol] = rate
    
    def add_exchange(self, exchange_name: str, exchange_info: str):
        """
        Ajouter ou mettre à jour une information d'échange dans le dictionnaire `exchanges`.
        
        :param exchange_name: Nom de l'échange
        :param exchange_info: Information de l'échange (par exemple, URL ou description)
        """
        self.exchanges[exchange_name] = exchange_info
    
    def get_index_price(self, symbol: str) -> float:
        """
        Récupérer le prix d'un indice à partir de son symbole.
        
        :param symbol: Symbole de l'indice
        :return: Le prix de l'indice
        """
        return self.index_price.get(symbol)
    
    def get_inert_state_rate(self, symbol: str) -> float:
        """
        Récupérer le taux d'état inertiel à partir de son symbole.
        
        :param symbol: Symbole du taux d'état inertiel
        :return: Le taux d'état inertiel
        """
        return self.inert_state_rate.get(symbol)

    def get_exchange_info(self, exchange_name: str) -> str:
        """
        Récupérer les informations d'un échange à partir de son nom.
        
        :param exchange_name: Nom de l'échange
        :return: Les informations de l'échange
        """
        return self.exchanges.get(exchange_name)

