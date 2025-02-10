from pydantic import BaseModel

class StockDataCreate(BaseModel):
    datetime: str
    open: float
    high: float
    low: float
    close: float
    volume: int
