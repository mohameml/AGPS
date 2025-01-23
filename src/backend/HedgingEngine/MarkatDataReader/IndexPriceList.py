from typing import List, Optional
from backend.HedgingEngine.MarkatDataReader.IndexPrice import IndexPrice
from backend.HedgingEngine.MarkatDataReader.GenericList import GenericList
# from IndexPrice import IndexPrice
# from GenericList import GenericList



class IndexPriceList(GenericList[IndexPrice]):
    """
    A specialized list for IndexPrice objects.
    """

    def get_price_by_index_name(self, index_name: str) -> Optional[IndexPrice]:
        """
        Retrieves the price of a given index by its name.

        Args:
            index_name (str): The name of the index to retrieve.

        Returns:
            Optional[IndexPrice]: The corresponding IndexPrice object if found, otherwise None.
        """
        for price in self.price_list:
            if price.index_name == index_name:
                return price
        return None




