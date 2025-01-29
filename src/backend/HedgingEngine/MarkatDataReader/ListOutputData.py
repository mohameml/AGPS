from typing import List
from backend.HedgingEngine.MarkatDataReader.OutputData import OutputData

class ListOutputData:

    def __init__(self):
        """Initialise une liste vide pour stocker les instances de OutputData."""
        self.data_list: List[OutputData] = []

    def add(self, output_data: OutputData):
        """Ajoute une instance de OutputData à la liste."""
        if not isinstance(output_data, OutputData):
            raise TypeError("L'élément ajouté doit être une instance de OutputData.")
        self.data_list.append(output_data)

    def __repr__(self) -> str:
        """Représentation lisible de la liste d'OutputData."""
        return f"ListOutputData(data_list={self.data_list})"

    def __len__(self) -> int:
        """Retourne le nombre d'éléments dans la liste."""
        return len(self.data_list)

    def __getitem__(self, index: int) -> OutputData:
        """Permet d'accéder aux éléments de la liste par index."""
        return self.data_list[index]