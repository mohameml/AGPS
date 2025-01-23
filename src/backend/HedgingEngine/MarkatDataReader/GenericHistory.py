from typing import Dict, TypeVar, Generic
from datetime import datetime

# Type générique pour représenter différents types de listes (IndexPriceList, InterestRateList, ExchangeRateList, etc.)
T = TypeVar('T')

class GenericHistory(Generic[T]):
    """
    A generic class to manage historical financial data.

    Attributes:
        records (Dict[datetime, T]): A dictionary storing financial data lists by date.
    """

    def __init__(self):
        """
        Initializes an empty historical data store.
        """
        self.records: Dict[datetime, T] = {}

    def add_record(self, date: datetime, data_list: T) -> None:
        """
        Adds a new data list for a specific date.

        Args:
            date (datetime): The date for which the data is recorded.
            data_list (T): The data list to store.
        """
        self.records[date] = data_list

    def get_record(self, date: datetime) -> T:
        """
        Retrieves the data list for a given date.

        Args:
            date (datetime): The date for which to retrieve the data.

        Returns:
            T: The corresponding data list.

        Raises:
            KeyError: If no record exists for the given date.
        """
        if date not in self.records:
            raise KeyError(f"No record found for date: {date}")
        return self.records[date]

    def list_dates(self) -> list:
        """
        Returns all the dates with stored records.

        Returns:
            list[datetime]: A list of stored dates.
        """
        return list(self.records.keys())

    def display_info(self) -> None:
        """
        Displays all stored records in a readable format.
        """
        if not self.records:
            print("No historical data available.")
        else:
            for date, data_list in self.records.items():
                print(f"\nDate: {date.strftime('%Y-%m-%d')}")
                if hasattr(data_list, "display_info"):
                    data_list.display_info()
                else:
                    print(data_list)
