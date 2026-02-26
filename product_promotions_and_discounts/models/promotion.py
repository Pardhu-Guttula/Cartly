# Epic Title: Store Promotion and Discount Data in PostgreSQL

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from backend import db

class Promotion(db.Model):
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), nullable=False, unique=True)
    discount_amount = Column(Integer, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    active = Column(Boolean, default=True)

    def __init__(self, code: str, discount_amount: int, expiry_date: datetime):
        self.code = code
        self.discount_amount = discount_amount
        self.expiry_date = expiry_date

    def is_valid(self) -> bool:
        return self.active and self.expiry_date > datetime.now()