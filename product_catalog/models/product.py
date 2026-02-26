# Epic Title: Design PostgreSQL data models for products

from backend import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    inventory = Column(Integer, nullable=False)

    category = relationship("Category", back_populates="products")

    def __init__(self, name: str, description: str, price: float, category_id: int, inventory: int):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.inventory = inventory