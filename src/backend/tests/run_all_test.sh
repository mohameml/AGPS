#!/bin/bash

# Ajouter le bon PYTHONPATH pour éviter les problèmes d'import
export PYTHONPATH=$(pwd):$PYTHONPATH

# Lancer tous les tests avec pytest
pytest backend/tests/ --tb=short --disable-warnings
