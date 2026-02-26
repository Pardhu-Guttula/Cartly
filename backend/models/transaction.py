# Epic Title: Implement Secure Checkout Process

from backend import db
from sqlalchemy import Column, Integer, String, Numeric, DateTime, func

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), nullable=False)
    payment_method = Column(String(50), nullable=False)
    transaction_date = Column(DateTime, server_default=func.now())

    def __init__(self, amount: float, status: str, payment_method: str):
        self.amount = amount
        self.status = status
        self.payment_method = payment_method