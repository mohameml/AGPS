import requests
import pytest
from datetime import datetime

BASE_URL = "http://localhost:3000"

@pytest.fixture
def portfolio_request_data():
    return {
        "cash" : 0 , 
        "compos" :  {"EUROSTOXX50": 0.0, "SP500": 0.0, "FTSE100": 0.0, "TOPIX": 0.0, "ASX200": 0.0 , "USD": 0.0, "GBP": 0.0, "JPY": 0.0, "AUD": 0.0},
        "date" : "2009-05-01T00:00:00",
        "isFirstTime" : True ,
        "currDate" : "2009-05-01T00:00:00"
    }

@pytest.fixture
def next_day_request_data():
    return {
        "date" : "2009-05-11T00:00:00"
    }

def test_hedge_endpoint(portfolio_request_data):
    response = requests.post(f"{BASE_URL}/hedge", json=portfolio_request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "output" in data["data"]
    assert "portfolio" in data["data"]

def test_next_day_endpoint(next_day_request_data):
    response = requests.get(f"{BASE_URL}/next-day", json=next_day_request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "date" in data["data"]
    assert "dict_index_price" in data["data"]
    assert "dict_exchange_rate" in data["data"]
