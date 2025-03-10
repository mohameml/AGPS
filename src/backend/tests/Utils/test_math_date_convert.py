import pytest
from datetime import datetime
import numpy as np 

from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter

def test_convert_to_math_distance():
    # Initialisation de l'objet MathDateConverter avec 252 jours ouvrés par an
    converter = MathDateConverter(workingDaysPerYear=252)

    # Cas de test 1: Conversion entre deux dates
    date_from = datetime(2023, 1, 1)
    date_until = datetime(2023, 1, 10)
    
    # Calcul attendu avec np.busday_count
    expected_distance = float(np.busday_count(date_from.date(), date_until.date()) / 252)
    
    # Vérification que la méthode retourne le bon résultat
    assert converter.ConvertToMathDistance(date_from, date_until) == expected_distance

def test_convert_to_math_distance_same_day():
    # Cas de test 2: Les deux dates sont les mêmes (distance mathématique devrait être 0)
    converter = MathDateConverter(workingDaysPerYear=252)
    
    date_from = datetime(2023, 1, 1)
    date_until = datetime(2023, 1, 1)

    assert converter.ConvertToMathDistance(date_from, date_until) == 0.0

def test_convert_to_math_distance_reverse_order():
    # Cas de test 3: Conversion de date_until avant date_from
    converter = MathDateConverter(workingDaysPerYear=252)

    date_from = datetime(2023, 1, 10)
    date_until = datetime(2023, 1, 1)

    # Cela devrait retourner un résultat négatif, selon l'ordre des dates
    expected_distance = float(np.busday_count(date_until.date(), date_from.date()) / 252)
    assert converter.ConvertToMathDistance(date_from, date_until) == expected_distance
