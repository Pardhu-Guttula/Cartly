from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: Implement Efficient Product Search Functionality

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    
    products = relationship("Product", back_populates="category")
    subcategories = relationship("Category", backref='parent', remote_side=[id])

    __table_args__ = (
        CheckConstraint('char_length(name) > 0', name='name_non_empty'),
    )