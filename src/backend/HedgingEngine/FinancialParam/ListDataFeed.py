from typing import List
import numpy as np
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed

class ListDataFeed:
    def __init__(self):
        self.data_feeds = []
    

    def addDataFeed(self , dataFeed : DataFeed) :
        self.data_feeds.append(dataFeed)

    def toDomesticMarket(self):
        """
        Applique la méthode toDomesticMarket() de chaque DataFeed
        et retourne une matrice où chaque ligne correspond aux données d'un DataFeed.
        """

        past = np.array([df.toDomesticMarket() for df in self.data_feeds])
        return past 
    
    def display_info(self):
        """Affiche les informations de chaque DataFeed dans la liste."""
        for df in self.data_feeds:
            df.display_info()