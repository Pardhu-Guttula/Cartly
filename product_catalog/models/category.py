# Epic Title: Design PostgreSQL data models for products

from backend import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    products = relationship("Product", back_populates="category")

    def __init__(self, name: str):
        self.name = name