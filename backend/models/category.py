# Epic Title: Design PostgreSQL Data Models for Products

from backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    products = relationship("Product", back_populates="category")

    def __init__(self, name: str):
        self.name = name