from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

# Epic Title: Integrate Promotion System with Payment System

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    discount = Column(Float, default=0.0)
    final_amount = Column(Float, nullable=False)
    promo_code = Column(String(20))
    status = Column(String(20), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    promotion_id = Column(Integer, ForeignKey('promotions.id'), nullable=True)
    promotion = relationship("Promotion")