# Epic Title: Ensure Data Integrity and Referential Integrity in Product-Category Models

from backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    products = relationship("Product", back_populates="category")
    subcategories = relationship("Category", lazy='joined', join_depth=1)

    def __init__(self, name: str, description: str, parent_id: int = None):
        self.name = name
        self.description = description
        self.parent_id = parent_id