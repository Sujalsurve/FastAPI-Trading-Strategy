from sqlalchemy import Column, Integer, DECIMAL, TIMESTAMP
from database import Base

class StockData(Base):
    __tablename__ = "stock_data"
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(TIMESTAMP, index=True)
    open = Column(DECIMAL)
    high = Column(DECIMAL)
    low = Column(DECIMAL)
    close = Column(DECIMAL)
    volume = Column(Integer)
