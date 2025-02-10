import unittest
from fastapi.testclient import TestClient
from main import app  # Remove direct import of calculate_moving_average_strategy
from strategy import moving_average_crossover
from database import get_db, SessionLocal

client = TestClient(app)

class TestAPI(unittest.TestCase):

    def test_fetch_data(self):
        response = client.get("/data")
        self.assertEqual(response.status_code, 200)
    
    def test_add_data(self):
        new_stock = {
            "datetime": "2025-02-10T10:00:00",
            "open": 120.5,
            "high": 125.0,
            "low": 118.0,
            "close": 122.5,
            "volume": 5000000
        }
        response = client.post("/data", json=new_stock)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_strategy_performance(self):
        response = client.get("/strategy/performance")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == "__main__":
    unittest.main()
