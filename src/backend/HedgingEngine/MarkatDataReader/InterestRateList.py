from dataclasses import dataclass
from typing import List, Optional
from backend.HedgingEngine.MarkatDataReader.InterestRate import InterestRate
from backend.HedgingEngine.MarkatDataReader.GenericList import GenericList 

# Liste des taux d'intérêt
class InterestRateList(GenericList[InterestRate]):
    """
    A specialized list for InterestRate objects.
    """
    pass


# class InterestRateList:
#     """
#     A class to manage a collection of InterestRate objects.

#     Attributes:
#         price_list (List[InterestRate]): A list storing index price entries.
#     """

#     def __init__(self, price_list: Optional[List[InterestRate]] = None):
#         """
#         Initializes the InterestRateList with an optional list of index prices.

#         Args:
#             price_list (Optional[List[InterestRate]]): Initial list of index prices. Default is an empty list.
#         """
#         self.price_list: List[InterestRate] = price_list if price_list is not None else []
#         self.length = len(self.price_list)

#     def add_price(self, index_price: InterestRate) -> None:
#         """
#         Adds a new index price to the list.

#         Args:
#             index_price (InterestRate): The index price to add to the list.
#         """
#         self.price_list.append(index_price)
#         self.length += 1

#     def remove_price(self, index_name: str) -> bool:
#         """
#         Removes an index price from the list by index name.

#         Args:
#             index_name (str): The name of the index to remove.

#         Returns:
#             bool: True if the index was found and removed, False otherwise.
#         """
#         for price in self.price_list:
#             if price.index_name == index_name:
#                 self.price_list.remove(price)
#                 self.length -= 1
#                 return True
        
#         return False

#     def get_price(self, index_name: str) -> Optional[InterestRate]:
#         """
#         Retrieves the price of a given index by its name.

#         Args:
#             index_name (str): The name of the index to retrieve.

#         Returns:
#             Optional[InterestRate]: The corresponding InterestRate object if found, otherwise None.
#         """
#         for price in self.price_list:
#             if price.index_name == index_name:
#                 return price
#         return None

#     def list_prices(self) -> List[InterestRate]:
#         """
#         Returns the complete list of index prices.

#         Returns:
#             List[InterestRate]: A list of all stored index prices.
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


