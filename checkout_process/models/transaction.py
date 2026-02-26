# Epic Title: Integrate multiple payment gateways

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from backend import db

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(50), nullable=False)
    payment_gateway = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, amount: float, status: str, payment_gateway: str):
        self.user_id = user_id
        self.amount = amount
        self.status = status
        self.payment_gateway = payment_gateway