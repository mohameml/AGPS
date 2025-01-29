# from dataclasses import dataclass
# from enum import Enum



# class EnumCountry(Enum) : 
#     MR = 'MR'
#     FR = 'FR'
#     US = 'US'






# @dataclass
# class Student :
#     name : str
#     age : int
#     country : EnumCountry 

#     def __post_init__(self):
#         if not isinstance(self.name, str):
#             raise ValueError("name must be a string.")
#         if not isinstance(self.age, int):
#             raise ValueError("age must be an integer.")
#         if not isinstance(self.country, EnumCountry):
#             raise ValueError("country must be a EnumCountry.")
        
#     def display_info(self) -> str:
#         return f"Name: {self.name}, Age: {self.age}, Country: {self.country.value}"
        


# student1 : Student = Student("John", 25 ,EnumCountry.US)
# print(student1.display_info())


# print("===============================")
# import pandas as pd


# # Exemple de DataFrame
# data = {
#     'A': [1, 2, 3], 
#     'B': ['a', 'b', 'c'],

        
#     }
# df = pd.DataFrame(data)

# # Parcourir les index et récupérer les lignes
# for index, row in df.iterrows():
#     print(f"Index: {index}, Ligne: {row.to_dict()}")

