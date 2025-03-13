# **Documentation Backend - HedgingEngine**

> Le projet backend est conçu pour fournir une API permettant de réaliser des calculs financiers avancés, y compris la gestion des risques et des stratégies de couverture (hedging). L'API interagit avec un moteur de couverture, `HedgingEngine`, qui est intégré via gRPC pour communiquer avec un pricer C++ externe. Le projet utilise FastAPI pour exposer l'API et gRPC pour la communication entre les différents services.

## 1. **Structure des dossiers et fichiers**

> `backend:` Le dossier principal contenant toute l'architecture du backend.

-   **`API/`**

    -   Ce dossier contient toutes les routes et logiques liées à l'API exposée par FastAPI.

-   **`HedgingEngine/`**

    > Ce dossier contient le moteur de couverture principal, qui encapsule les différents composants nécessaires à la gestion financière et aux calculs.

    -   **`FinancialEstimator`** : Composant responsable des estimations financières, comme les taux d'intérêt ou les volatilités.
    -   **`FinancialParam`** : Contient les paramètres financiers nécessaires aux calculs .
    -   **`Hedging`** : Logique principale de couverture, calcul des stratégies de couverture basées sur les estimations financières et le portefeuille.
    -   **`MarketDataReader`** : Permet de lire les données du marché, telles que les prix des actifs, les historiques des prix, etc.
    -   **`Portfolio`** : Gère les informations relatives au portefeuille, telles que la composition des actifs, les positions, etc.
    -   **`Pricer`** : Interface de communication avec le pricer en C++ via gRPC pour effectuer les calculs de pricing des produits dérivés.

-   **`protos/`**

    > Contient les fichiers de définition des services gRPC `pricing.proto`.

-   **`tests/`**

    > Ce dossier contient les tests unitaires et d'intégration pour valider la logique de l'API, du moteur de couverture et des composants individuels.

-   **`app.py`**

    > Le point d'entrée principal du backend, où FastAPI est initialisé et où les routes API sont définies.

-   **`server.py`**

    > Le fichier responsable du lancement du serveur FastAPI, où le serveur web est configuré et démarré.

## 2. **Installation et Lancement:**

-   **Prérequis**

    -   Python 3.8+
    -   FastAPI
    -   gRPC
    -   Protoc (pour compiler les fichiers `.proto`)

-   **Installation**

    -   Installez les dépendances :

        ```bash
        pip install -r requirements.txt
        ```

    -   Compilez les fichiers `.proto` pour générer les fichiers Python gRPC :
        ```bash
        python3 -m grpc_tools.protoc -I=./protos --python_out=./HedgingEngine/Pricer --grpc_python_out=./HedgingEngine/Pricer ./protos/pricing.proto
        ```

-   **Exécution du serveur**

    Pour démarrer l'application FastAPI (depuis le dossier `src/`) :

    ```bash
     uvicorn backend.app:app --host 127.0.0.1 --port 3000 --reload
    ```

    ou :

    ```bash
    python -m backend.server
    ```

## 3. **Test et Validation**

> Les tests sont définis dans le dossier `tests/` pour chaque composant. Ils permettent de vérifier la logique du moteur de couverture et les interactions gRPC.

-   **lancer le test:**

```bash
export PYTHONPATH=$(pwd):$PYTHONPATH
pytest backend/tests/NomDossierTest/nom_fichier_test.py
```
