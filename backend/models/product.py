from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

# Epic Title: Develop Reusable Product Browsing Components

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True, default=0.0)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    inventory = Column(Integer, nullable=False)
    
    category = relationship("Category", back_populates="products")