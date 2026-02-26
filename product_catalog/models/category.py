# Epic Title: Design PostgreSQL data models for categories

from backend import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(512), nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    children = relationship("Category", back_populates="parent", remote_side=[id])
    parent = relationship("Category", back_populates="children", remote_side=[parent_id])
    products = relationship("Product", back_populates="category")

    def __init__(self, name: str, description: str, parent_id: int = None):
        self.name = name
        self.description = description
        self.parent_id = parent_id