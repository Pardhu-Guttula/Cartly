from sqlalchemy import Column, Integer, String, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: Ensure Data Integrity and Referential Integrity in Product-Category Models

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    inventory = Column(Integer, nullable=False)
    
    category = relationship("Category", back_populates="products")

    __table_args__ = (
        CheckConstraint('price > 0', name='price_positive'),
        CheckConstraint('inventory >= 0', name='inventory_non_negative'),
    )