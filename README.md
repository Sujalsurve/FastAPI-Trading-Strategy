# FastAPI Trading Strategy

## 📌 Project Overview
This project is a **FastAPI-based** trading strategy application that stores stock market data and implements a **Moving Average Crossover Strategy** to generate buy/sell signals. It uses **PostgreSQL** as the database and is containerized with **Docker**.

## 🚀 Features
- **RESTful API** for fetching and adding stock data.
- **Moving Average Crossover Strategy** for generating trading signals.
- **Database persistence** using PostgreSQL.
- **Containerized application** with Docker.

---

## 📂 Project Structure
```
FASTAPI_TRADING_STRATEGY/
│── __pycache__/             # Compiled Python files
│── venv/                    # Virtual environment (dependencies)
│── .coverage                # Coverage report for tests
│── .env                     # Environment variables (database credentials, etc.)
│── database.py               # Database connection and session management
│── docker-compose.yml        # Docker configuration file
│── Dockerfile                # Docker build file for containerization
│── main.py                   # Main FastAPI application
│── models.py                 # SQLAlchemy models (database schema)
│── requirements.txt           # List of dependencies for the project
│── schemas.py                 # Pydantic models for request validation
│── strategy.py                # Trading strategy implementation (Moving Averages)
│── test_main.py               # Unit tests for API and logic

```

---

## 🛠 Setup & Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Sujalsurve/fastapi_trading_strategy.git
cd fastapi_trading_strategy
```

### 2️⃣ Create & Activate Virtual Environment (Optional)
```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up PostgreSQL Database (If Not Using Docker)
```sh
psql -U postgres
CREATE DATABASE stock_db;
```

### 5️⃣ Run the Application
```sh
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

---

## 🐳 Running with Docker

### 1️⃣ Build & Start Containers
```sh
docker-compose up --build
```

### 2️⃣ Stop Containers
```sh
docker-compose down
```

---

## 📡 API Endpoints

### ✅ Fetch All Stock Data
```http
GET /data
```
Response:
```json
[
  {"id": 1, "datetime": "2024-01-24T00:00:00", "close": 113.15, "volume": 5737135},
  {"id": 2, "datetime": "2024-01-27T00:00:00", "close": 112.00, "volume": 8724577}
]
```

### ✅ Add New Stock Data
```http
POST /data
```
Body:
```json
{
  "datetime": "2024-02-10T10:00:00",
  "open": 100.5,
  "high": 105.2,
  "low": 99.8,
  "close": 104.1,
  "volume": 500000
}
```

### ✅ Get Moving Average Crossover Strategy
```http
GET /strategy/performance
```
Response:
```json
[
  {"datetime": "2024-02-05T00:00:00", "close": 102.4, "signal": "BUY"},
  {"datetime": "2024-02-06T00:00:00", "close": 104.65, "signal": "SELL"}
]
```

---

## 🔬 Running Unit Tests
```sh
pytest test_main.py --cov=app
```

---

## 💡 Future Enhancements
- Implement **real-time stock data fetching**.
- Improve **error handling** and **logging**.
- Add **user authentication** and **role-based access control**.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request (PR)

---

## 📞 Contact
For any issues, please raise an **issue** on GitHub or contact:
- **number**: 91+8767483019
- **Email**: sujalsurve13@gmail.com
- **GitHub**: [Sujalsurve](https://github.com/Sujalsurve?tab=repositories)

