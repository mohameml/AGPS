from backend.HedgingEngine.MarkatDataReader.IndexPriceList import IndexPriceList
from backend.HedgingEngine.MarkatDataReader.GenericHistory import GenericHistory
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex

class IndexPriceHistory(GenericHistory[IndexPriceList]):
    """
    A specialized class to manage historical index prices.
    """
    
    def get_all_price_by_index_name(self ,index_name : EnumIndex) :
        """retrun : list of  price for the index_name """
        list_price = []
        for date in self.records.keys() :
            list_price.append(self.records[date].get_price_by_index_name(index_name))

        return list_price

    def get_all_price_for_all_index_name(self):
        matrix_price = []

        for index_name in EnumIndex : 
            list_price = self.get_all_price_by_index_name(index_name)
            matrix_price.append(list_price)
        return matrix_price



