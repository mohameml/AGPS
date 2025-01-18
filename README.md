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


- **PricerEngine:**

```bash
cd PricerEngine/
mkdir build
cd build/
cmake -DCMAKE_PREFIX_PATH=/path/to/pnl/build ..
make
./pricing_server
```