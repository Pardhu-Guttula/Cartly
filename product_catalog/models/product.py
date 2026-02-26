# Epic Title: Implement product management functionality

from datetime import datetime
from backend import db
from sqlalchemy import Column, Integer, String, Float, Text, DateTime

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price