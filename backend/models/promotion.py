from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Epic Title: Integrate Promotion System with Payment System

Base = declarative_base()

class Promotion(Base):
    __tablename__ = 'promotions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), nullable=False, unique=True)
    description = Column(String(255), nullable=False)
    discount_amount = Column(Float, nullable=False)
    expiration_date = Column(Date, nullable=False)
    
    def is_valid(self) -> bool:
        return datetime.utcnow().date() <= self.expiration_date