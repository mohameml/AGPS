from backend.HedgingEngine.MarkatDataReader.IndexPriceList import IndexPriceList
from backend.HedgingEngine.MarkatDataReader.GenericHistory import GenericHistory

class IndexPriceHistory(GenericHistory[IndexPriceList]):
    """
    A specialized class to manage historical index prices.
    """
    pass



# class IndexPriceHistory:
#     """
#     A class to manage historical index prices.

#     Attributes:
#         index_price_records (Dict[datetime, IndexPriceList]):  A dictionary storing index price lists by date.
#     """

#     def __init__(self):
#         """
#         Initializes an empty index price history.
#         """
#         self.index_price_records: Dict[datetime, IndexPriceList] = {}

#     def add_price_list(self, date: datetime, index_price_list: IndexPriceList) -> None:
#         """
#         Adds a new index price list for a specific date.

#         Args:
#             date (datetime): The date for which the prices are recorded.
#             index_price_list (IndexPriceList): The list of index prices to store.
#         """
#         self.index_price_records[date] = index_price_list

#     def get_price_list(self, date: datetime) -> IndexPriceList:
#         """
#         Retrieves the index price list for a given date.

#         Args:
#             date (datetime): The date for which to retrieve the prices.

#         Returns:
#             IndexPriceList: The corresponding price list.

#         Raises:
#             KeyError: If no record exists for the given date.
#         """
#         if date not in self.index_price_records:
#             raise KeyError(f"No index price record found for date: {date}")
#         return self.index_price_records[date]

#     def list_dates(self) -> list:
#         """
#         Returns all the dates with stored index price records.

#         Returns:
#             list[datetime]: A list of stored dates.
#         """
#         return list(self.index_price_records.keys())

#     def display_info(self) -> None:
#         """
#         Displays all stored index price records in a readable format.
#         """
#         if not self.index_price_records:
#             print("No index price history available.")
#         else:
#             for date, price_list in self.index_price_records.items():
#                 print(f"\nDate: {date.strftime('%Y-%m-%d')}")
#                 price_list.display_info()

