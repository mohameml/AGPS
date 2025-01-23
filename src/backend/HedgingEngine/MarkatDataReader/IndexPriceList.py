from typing import List, Optional
from backend.HedgingEngine.MarkatDataReader.IndexPrice import IndexPrice
from backend.HedgingEngine.MarkatDataReader.GenericList import GenericList

class IndexPriceList(GenericList[IndexPrice]):
    """
    A specialized list for IndexPrice objects.
    """

    def get_price(self, index_name: str) -> Optional[IndexPrice]:
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



# class IndexPriceList:
#     """
#     A class to manage a collection of IndexPrice objects.

#     Attributes:
#         price_list (List[IndexPrice]): A list storing index price entries.
#     """

#     def __init__(self, price_list: Optional[List[IndexPrice]] = None):
#         """
#         Initializes the IndexPriceList with an optional list of index prices.

#         Args:
#             price_list (Optional[List[IndexPrice]]): Initial list of index prices. Default is an empty list.
#         """
#         self.price_list: List[IndexPrice] = price_list if price_list is not None else []
#         self.length = len(self.price_list)

#     def add_price(self, index_price: IndexPrice) -> None:
#         """
#         Adds a new index price to the list.

#         Args:
#             index_price (IndexPrice): The index price to add to the list.
#         """
#         self.price_list.append(index_price)
#         self.length += 1

        

#     def get_price(self, index_name: str) -> Optional[IndexPrice]:
#         """
#         Retrieves the price of a given index by its name.

#         Args:
#             index_name (str): The name of the index to retrieve.

#         Returns:
#             Optional[IndexPrice]: The corresponding IndexPrice object if found, otherwise None.
#         """
#         for price in self.price_list:
#             if price.index_name == index_name:
#                 return price
#         return None

#     def list_prices(self) -> List[IndexPrice]:
#         """
#         Returns the complete list of index prices.

#         Returns:
#             List[IndexPrice]: A list of all stored index prices.
#         """
#         return self.price_list

#     def display_info(self) -> None:
#         """
#         Displays all index prices in a formatted way.
#         """
#         if not self.price_list:
#             print("No index prices available.")
#         else:
#             for price in self.price_list:
#                 print(price.display_info())


