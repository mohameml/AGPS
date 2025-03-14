import requests
import pytest
from datetime import datetime

BASE_URL = "http://localhost:3000"

@pytest.fixture
def portfolio_request_data():
    return {
        "cash": 10000.0,
        "compos": {"AAPL": 50, "GOOGL": 30},
        "date": datetime.utcnow().isoformat(),
        "isFirstTime": True,
        "currDate": datetime.utcnow().isoformat()
    }

@pytest.fixture
def next_day_request_data():
    return {
        "date": datetime.utcnow().isoformat()
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
