# AGPS : application de gestion de prosuit structuré


- **frontend:**

```bash
cd frontend/
npm install 
npm run dev 
```

- **backend:**

```bash
cd backend/
python3 -m venv .venv
source .venv/bin/activate
which python3  
pip install -r requirements.txt
uvicorn main:app --reload
```

```bash
python -m backend.tests.test_market_data_reader  
```

- **PricerEngine:**

```bash
cd PricerEngine/
mkdir build
cd build/
cmake -DCMAKE_PREFIX_PATH=/path/to/pnl/build ..
make
./pricing_server
```


<!-- - backend :
    - HedgingEnginr :
        - MarketDataReader :
            - IndexPrice.py
            - __inti__.py
        __init__.py 

    - tests :
        - test.py 

    - __init__.py  -->


