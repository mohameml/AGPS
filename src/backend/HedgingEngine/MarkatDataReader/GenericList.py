from dataclasses import dataclass, field
from typing import Generic, TypeVar, List


T = TypeVar('T')

@dataclass
class GenericList(Generic[T]):
    """
    - A generic list class to hold financial data elements.

    - Attributes:
        - items (List[T]): A list containing elements of type T.
    """

    items: List[T] = field(default_factory=list)

    def add(self, item: T) -> None:
        """
        Adds an item to the list.
        """
        self.items.append(item)

    def get(self, index: int) -> T:
        """
        Returns the item at the specified index.   
        """
        return self.items[index]

    def get_all(self) -> List[T]:
        """
        Returns all items in the list.
        """
        return self.items

    def __len__(self) -> int:
        """
        Returns the number of items in the list.
        """
        return len(self.items)

    def __str__(self) -> str:
        """
        Returns a string representation of the list.
        """        
        return f"{[item for item in self.items]}"

    def display_info(self) -> None : 
        if not self.items :
            print("No Data available.")
        else : 
            for item in self.items :
                print(item.display_info())
