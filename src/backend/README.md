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

## 4. **Documentation de l'API:**

> Cette API fournit deux endpoints principaux pour la gestion et la simulation de couverture d'un portefeuille financier.

### 4.1. **`/hedge` (POST):**

-   **Description:**

    > Cet endpoint permet d'effectuer une couverture sur un portefeuille donné en fonction de ses compositions, du montant de cash disponible, et de la date d'analyse.

-   **Requête:**

    -   **URL** : `/hedge`
    -   **Méthode** : `POST`
    -   **Body (JSON, format `PortfolioDataRequest`)** :

    ```json
    {
    	"cash": 10000.0,
    	"compos": { "AAPL": 50, "GOOGL": 30 },
    	"date": "2025-03-14T00:00:00",
    	"isFirstTime": true,
    	"currDate": "2025-03-14T00:00:00"
    }
    ```

-   **Modèle de la requête (`PortfolioDataRequest`):**

    | Champ         | Type               | Description                                                                      |
    | ------------- | ------------------ | -------------------------------------------------------------------------------- |
    | `cash`        | `float`            | Montant de cash disponible dans le portefeuille.                                 |
    | `compos`      | `Dict[str, float]` | Dictionnaire représentant les compositions du portefeuille (ticker -> quantité). |
    | `date`        | `datetime`         | Date d'analyse du portefeuille.                                                  |
    | `isFirstTime` | `bool`             | Indique si c'est la première couverture effectuée.                               |
    | `currDate`    | `datetime`         | Date actuelle de la requête.                                                     |

-   **Réponse:**

    ```json
    {
    	"status": "success",
    	"data": {
    		"output": {
    			"date": "2025-03-14T00:00:00",
    			"value": 105000.0,
    			"deltas": [0.1, -0.2],
    			"deltas_std_dev": [0.01, 0.02],
    			"price": 3500.0,
    			"price_std_dev": 15.0
    		},
    		"portfolio": {
    			"compositions": { "AAPL": 50, "GOOGL": 30 },
    			"cash": 5000.0,
    			"date": "2025-03-14T00:00:00",
    			"value": 105000.0
    		}
    	}
    }
    ```

-   **Modèles de la réponse:**

    -   **`OutputData` :**

        | Champ            | Type          | Description                                       |
        | ---------------- | ------------- | ------------------------------------------------- |
        | `date`           | `datetime`    | Date du calcul de la couverture.                  |
        | `value`          | `float`       | Valeur totale du portefeuille après couverture.   |
        | `deltas`         | `List[float]` | Liste des deltas des actifs dans le portefeuille. |
        | `deltas_std_dev` | `List[float]` | Écart-type des deltas calculés.                   |
        | `price`          | `float`       | Prix total du portefeuille.                       |
        | `price_std_dev`  | `float`       | Écart-type du prix.                               |

    -   **`Portfolio`:**

        | Champ          | Type               | Description                                     |
        | -------------- | ------------------ | ----------------------------------------------- |
        | `compositions` | `Dict[str, float]` | Composition du portefeuille.                    |
        | `cash`         | `float`            | Montant de cash restant.                        |
        | `date`         | `datetime`         | Date de la mise à jour.                         |
        | `value`        | `float`            | Valeur totale du portefeuille après couverture. |

### 4.2. **`/next-day` (GET):**

-   **Description:**

    > Cet endpoint permet d'obtenir les données de marché du jour suivant en fonction de la date fournie.

-   **Requête:**

    -   **URL** : `/next-day`
    -   **Méthode** : `GET`
    -   **Body (JSON, format `NextDayRequest`)** :

    ```json
    {
    	"date": "2025-03-14T00:00:00"
    }
    ```

-   **Modèle de la requête (`NextDayRequest`):**

    | Champ  | Type       | Description                                                   |
    | ------ | ---------- | ------------------------------------------------------------- |
    | `date` | `datetime` | Date de référence pour récupérer les données du jour suivant. |

-   **Réponse:**

    ```json
    {
    	"status": "success",
    	"data": {
    		"date": "2025-03-15T00:00:00",
    		"dict_index_price": {
    			"SP500": 4800.5,
    			"NASDAQ": 15000.3
    		},
    		"dict_exchange_rate": {
    			"USD": 1.1,
    			"JPY": 130.5
    		}
    	}
    }
    ```

-   **Modèle de la réponse:**

    | Champ                | Type               | Description                                  |
    | -------------------- | ------------------ | -------------------------------------------- |
    | `date`               | `datetime`         | Date du jour suivant.                        |
    | `dict_index_price`   | `Dict[str, float]` | Dictionnaire des prix des indices boursiers. |
    | `dict_exchange_rate` | `Dict[str, float]` | Dictionnaire des taux de change des devises. |

### 4.3 **Pour tester l'API localement:**

-   **lancer le serveur Cpp:**

    ```bash
    cd backend/tests/Pricer/serverCpp
    mkdir build
    cd build
    cmake -DCMAKE_PREFIX_PATH=path/to/protoc ..
    make
    ./pricing_server
    ```

-   **lancer serveur uvicorn:**

    ```bash
    uvicorn backend.app:app --host 127.0.0.1 --port 3000 --reload
    ```

    RQ : il faut lancer depuis le dossier `src/`

-   **Tester l'API:**

    -   **`Tester /hedge (POST)`:**

        ```bash
        curl -X POST http://localhost:3000/hedge \
            -H "Content-Type: application/json" \
            -d '{
                "cash" : 0 ,
                "compos" :  {"EUROSTOXX50": 0.0, "SP500": 0.0, "FTSE100": 0.0, "TOPIX": 0.0, "ASX200": 0.0 , "USD": 0.0, "GBP": 0.0, "JPY": 0.0, "AUD": 0.0},
                "date" : "2009-05-01T00:00:00",
                "isFirstTime" : true ,
                "currDate" : "2009-05-01T00:00:00"
            }'
        ```

    -   **`Tester /next-day (GET)`:**

        ```bash
        curl -X GET http://localhost:8000/next-day \
            -H "Content-Type: application/json" \
            -d '{
                "date": "2009-05-11T00:00:00"
                }'
        ```

    RQ : vous pouvez aussi utiliser `postman`
