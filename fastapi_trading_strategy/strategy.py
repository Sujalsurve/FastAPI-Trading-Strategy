import pandas as pd
import numpy as np
from sqlalchemy.orm import Session
from models import StockData

def moving_average_crossover(db: Session):
    stock_data = db.query(StockData).order_by(StockData.datetime).all()

    if not stock_data:
        return {"error": "No data available"}

    # Convert database results to DataFrame
    df = pd.DataFrame([{
        "datetime": s.datetime,
        "close": float(s.close)
    } for s in stock_data])

    # Ensure sufficient data for moving averages
    if len(df) < 20:
        return {"error": "Not enough data for moving average calculation (need at least 20 records)"}

    # Calculate short-term and long-term moving averages
    df["short_ma"] = df["close"].rolling(window=5, min_periods=1).mean()
    df["long_ma"] = df["close"].rolling(window=20, min_periods=1).mean()

    # Generate buy/sell signals
    df["signal"] = np.where(df["short_ma"] > df["long_ma"], "BUY", "SELL")
    df["signal"].fillna("HOLD", inplace=True)  # Fill NaNs with "HOLD"

    return df.tail(10).to_dict(orient="records")
