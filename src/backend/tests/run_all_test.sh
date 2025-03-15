#!/bin/bash

# Activer le mode strict pour détecter les erreurs
set -e

# Définir des couleurs pour les logs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # Pas de couleur

echo -e "${YELLOW}📌 Activation de l'environnement virtuel...${NC}"
cd ../../  # Aller à la racine du projet (src/)
if [ -d "backend/.venv" ]; then
    source backend/.venv/bin/activate
else
    echo -e "${RED}⚠️  Environnement virtuel introuvable. Exécutez : python -m venv venv${NC}"
    exit 1
fi

# echo -e "${YELLOW}📌 Installation des dépendances Python...${NC}"
# pip install --quiet --no-cache-dir -r backend/requirements.txt

echo -e "${YELLOW}📌 Lancement du serveur backend...${NC}"
uvicorn backend.app:app --host 127.0.0.1 --port 3000 --reload &  
BACKEND_PID=$!  # Récupérer le PID du serveur backend

sleep 3  # Attendre quelques secondes que le backend démarre

echo -e "${YELLOW}📌 Compilation et lancement du serveur C++...${NC}"
cd backend/tests/Pricer/serverCpp/   
mkdir -p build
cd build
cmake -DCMAKE_PREFIX_PATH=$HOME/.local .. && make  
./pricing_server &  
CPP_SERVER_PID=$!

sleep 2  # Attendre le démarrage du serveur C++

echo -e "${YELLOW}📌 Exécution des tests avec pytest...${NC}"
cd ../../../../../  # Revenir à la racine du projet (src/)
echo $(pwd)
export PYTHONPATH=$(pwd):$PYTHONPATH
pytest backend/tests/ --tb=short --disable-warnings | tee  backend/tests/pytest_report.txt

# Vérifier si les tests ont réussi ou échoué
if grep -q "failed" pytest_report.txt; then
    echo -e "${RED}❌ Certains tests ont échoué. Consultez pytest_report.txt.${NC}"
else
    echo -e "${GREEN}✅ Tous les tests ont réussi !${NC}"
fi

# Arrêter les serveurs
echo -e "${YELLOW}📌 Arrêt des serveurs...${NC}"
kill $BACKEND_PID
kill $CPP_SERVER_PID

echo -e "${GREEN}🎉 Fin du script.${NC}"
