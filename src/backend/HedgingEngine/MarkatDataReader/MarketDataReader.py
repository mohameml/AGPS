from datetime import datetime
from typing import List, Dict
import pandas as pd
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.MarkatDataReader.EnumIndex import index_to_currency
from backend.HedgingEngine.MarkatDataReader.IndexPriceHistory import IndexPriceHistory
from backend.HedgingEngine.MarkatDataReader.IndexPrice import IndexPrice
from backend.HedgingEngine.MarkatDataReader.IndexPriceList import IndexPriceList
from backend.HedgingEngine.MarkatDataReader.InterestRateHistory import InterestRateHistory
from backend.HedgingEngine.MarkatDataReader.InterestRateList import InterestRateList
from backend.HedgingEngine.MarkatDataReader.InterestRate import InterestRate
from backend.HedgingEngine.MarkatDataReader.ExchangeRateHistory import ExchangeRateHistory
from backend.HedgingEngine.MarkatDataReader.ExchangeRateList import ExchangeRateList
from backend.HedgingEngine.MarkatDataReader.ExchangeRate import ExchangeRate
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed


class MarketDataReader:
    """
    - Classe responsable de la lecture des données de marché à partir d'un fichier et de la gestion des indices,  des taux de change et des taux d'intérêt.

    - Attributes:
        - file_path (str): Chemin du fichier contenant les données de marché.
        - indexes (List[EnumIndex]): Liste des indices à analyser.
        - T0 (date): Date de début de la période d'analyse.
        - T (date): Date de fin de la période d'analyse.
    """

    def __init__(self, file_path: str, indexes: List[EnumIndex], T0: datetime, T: datetime):
        """
        Initialise la classe MarketDataReader avec les paramètres donnés.
        """
        self.file_path : str = file_path
        self.indexes : List[EnumIndex] = indexes
        self.T0 : datetime = T0
        self.T : datetime = T
    
        try :
            self.data_index_price: pd.DataFrame = pd.read_excel(self.file_path  , sheet_name = 'ClosePrice')
            self.data_exchange_rate: pd.DataFrame = pd.read_excel(self.file_path  , sheet_name = 'XFORPrice')
            self.data_interest_rate: pd.DataFrame = pd.read_excel(self.file_path  , sheet_name = 'TauxInteret')
        except Exception as e : 
            
            raise RuntimeError(f"Erreur lors du chargement du fichier {self.file_path}.\n{e}")
        
        self.data_index_price = self.clean_data(self.data_index_price , filter_names=[e.value for e in self.indexes])
        self.data_interest_rate = self.clean_data(self.data_interest_rate , filter_names=[f'R{index_to_currency[e].value}' for e in self.indexes])
        filter_names_exchange_rate = [f'X{index_to_currency[e].value}' for e in self.indexes]
        filter_names_exchange_rate.remove('XEUR')
        self.data_exchange_rate = self.clean_data(self.data_exchange_rate , filter_names= filter_names_exchange_rate)

        # self.filter_common_valid_dates()


        self._exchange_rate_history: ExchangeRateHistory = ExchangeRateHistory()
        self._index_price_history: IndexPriceHistory = IndexPriceHistory()
        self._interest_rate_history: InterestRateHistory = InterestRateHistory()
        

        self.extract_index_price_history()
        self.extract_interest_rate_history()
        self.extract_exchange_rate_history()




    def clean_data(self , df : pd.DataFrame , filter_names : List[str]) -> None : 
        filter_names.append('Date')
        df = df[filter_names]
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df[(df.Date >= self.T0) & (df.Date <= self.T)]
        df = df.set_index('Date')
        df = df.dropna()

        return df 
    
    def filter_common_valid_dates(self):
        """
        Filtre les trois DataFrames pour ne garder que les dates où toutes les valeurs sont valides.
        """
        common_dates = (
            self.data_index_price.dropna().index
            & self.data_exchange_rate.dropna().index
            & self.data_interest_rate.dropna().index
        )

        self.data_index_price = self.data_index_price.loc[common_dates]
        self.data_exchange_rate = self.data_exchange_rate.loc[common_dates]
        self.data_interest_rate = self.data_interest_rate.loc[common_dates]
        

    def extract_index_price_history(self) -> None:
        """Extrait les données des prix des indices depuis data_index_price."""

        for date , row in self.data_index_price.iterrows() :
            row_dict = row.to_dict()
            index_price_list = IndexPriceList()
            for key , value in row_dict.items() :
                enum_index = EnumIndex.str_to_enum(key)
                enum_curr = index_to_currency[enum_index]
                index_price = IndexPrice(enum_index , enum_curr , value)
                index_price_list.add(index_price)
            self._index_price_history.add_record(date , index_price_list)
            



    def extract_interest_rate_history(self) -> None:
        """Extrait les données des taux d'intérêt depuis le fichier source."""

        for date , row in self.data_interest_rate.iterrows() : 
            row_dict = row.to_dict()
            interest_rate_list = InterestRateList()
            for key , value in row_dict.items() :
                enum_curr = EnumCurrency.str_to_enum(key[1:])
                interest_rate = InterestRate(enum_curr , value)
                interest_rate_list.add(interest_rate)
            self._interest_rate_history.add_record(date , interest_rate_list)

    def extract_exchange_rate_history(self) -> None:
        
        for date , row in self.data_exchange_rate.iterrows() : 
            row_dict = row.to_dict()
            exchange_rate_list = ExchangeRateList()
            for key , value in row_dict.items() :
                enum_curr = EnumCurrency.str_to_enum(key[1:])
                exchange_rate = ExchangeRate(enum_curr , value , EnumCurrency.EUR)
                exchange_rate_list.add(exchange_rate)
            self._exchange_rate_history.add_record(date , exchange_rate_list)


    def get_nb_days_in_one_year(self , year : int) -> int :
        """
        Retourne le nombre de jours dans une année pour une date donnée.
        """
        nb_jours = sum([1 for date in self._index_price_history.records.keys() if date.year == year])
        return nb_jours


    def get_data_feed(self, date: datetime) -> DataFeed:
        """
        Récupère les données du marché pour une date spécifique.
        """
        if date not in self._index_price_history.records.keys() or date not in self._exchange_rate_history.records.keys() :
            raise ValueError(f"La date {date} n'est pas dans la période d'analyse.")

        dict_index_prices : Dict[EnumIndex , IndexPrice] = {}
        dict_exchanges : Dict [EnumCurrency , ExchangeRate]= {}

        for index_price in self._index_price_history.records[date].items:
            dict_index_prices[index_price.index_name] = index_price


        for exchange_rate in self._exchange_rate_history.records[date].items:
            dict_exchanges[exchange_rate.base_currency] = exchange_rate
        

        data_feed = DataFeed(date , dict_index_prices , dict_exchanges)

        return data_feed

    # def get_all_data_feed(self) -> List[DataFeed]:
    #     """
    #     Récupère les données du marché pour toutes les dates de la période d'analyse sous forme List[DataFeed].
    #     """
    #     # il faut parcourir les dates et appler get_data_feed pour chaque date
    #     data_feeds = []
    #     for date in self._index_price_history.records.keys():
    #         data_feeds.append(self.get_data_feed(date))
    #     return data_feeds
    
    # def get_list_data_feed(self , finical_params) :
    #     """
    #     Récupère les données du marché pour toutes les dates de la période d'analyse sous forme ListDataFeed.
    #     """
    #     from backend.HedgingEngine.FinancialParam.ListDataFeed import ListDataFeed

    #     data_feeds = ListDataFeed(finical_params)
    #     for date in self._index_price_history.records.keys():
    #         data_feeds.addDataFeed(self.get_data_feed(date))
    #     return data_feeds
    
