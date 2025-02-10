from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import StockData
from schemas import StockDataCreate
from strategy import moving_average_crossover

app = FastAPI()

# ✅ Fetch all stock data
@app.get("/data")
def get_all_data(db: Session = Depends(get_db)):
    try:
        data = db.query(StockData).all()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Add new stock data
@app.post("/data")
def add_data(stock: StockDataCreate, db: Session = Depends(get_db)):
    try:
        new_record = StockData(**stock.model_dump())  # ✅ Updated for Pydantic v2
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return {"message": "Data added successfully", "data": new_record}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Get Moving Average Crossover strategy signals
@app.get("/strategy/performance")
def get_strategy_performance(db: Session = Depends(get_db)):
    try:
        result = moving_average_crossover(db)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
