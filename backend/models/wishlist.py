from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

Base = declarative_base()

class Wishlist(Base):
    __tablename__ = 'wishlists'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, unique=True)

    items = relationship("WishlistItem", back_populates="wishlist")