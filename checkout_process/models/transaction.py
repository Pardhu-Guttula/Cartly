# Epic Title: Implement secure checkout process

from datetime import datetime
from backend import db
from sqlalchemy import Column, Integer, String, Float, DateTime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, product_id: int, amount: float, status: str):
        self.user_id = user_id
        self.product_id = product_id
        self.amount = amount
        self.status = status