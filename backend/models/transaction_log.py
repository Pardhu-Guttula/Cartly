from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Epic Title: Log and store transactions securely

Base = declarative_base()

class TransactionLog(Base):
    __tablename__ = 'transaction_logs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(String(50), nullable=False)
    order_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(50), nullable=False)
    payment_gateway = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)