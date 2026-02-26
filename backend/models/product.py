# Epic Title: Design PostgreSQL Data Models for Products

from backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    inventory = Column(Integer, nullable=False)

    category = relationship("Category", back_populates="products")

    def __init__(self, name: str, description: str, price: float, category_id: int, inventory: int):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.inventory = inventory