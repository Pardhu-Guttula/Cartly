# Epic Title: Integrate Promotion System with Payment System

from sqlalchemy import Column, Integer, String, DECIMAL
from backend import db

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(DECIMAL(10, 2), nullable=False)
    promotion_code = Column(String(50), nullable=True)

    def __init__(self, amount: float, promotion_code: str = None):
        self.amount = amount
        self.promotion_code = promotion_code