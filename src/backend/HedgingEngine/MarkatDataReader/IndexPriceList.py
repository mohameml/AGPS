from typing import Optional
from backend.HedgingEngine.MarkatDataReader.IndexPrice import IndexPrice
from backend.HedgingEngine.MarkatDataReader.GenericList import GenericList
from backend.HedgingEngine.MarkatDataReader.EnumIndex import EnumIndex



class IndexPriceList(GenericList[IndexPrice]):
    """
    A specialized list for IndexPrice objects.
    """

    def get_price_by_index_name(self, index_name: EnumIndex) :
        """
        Retrieves the price of a given index by its name.
        """
        if not isinstance(index_name , EnumIndex) :
            raise ValueError("the index name must be a EnumIndex")

        for price in self.price_list:
            if price.index_name == index_name:
                return price
        return None




