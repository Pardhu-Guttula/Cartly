from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

Base = declarative_base()

class WishlistItem(Base):
    __tablename__ = 'wishlist_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    wishlist_id = Column(Integer, ForeignKey('wishlists.id'), nullable=False)
    product_id = Column(Integer, nullable=False)
    
    wishlist = relationship("Wishlist", back_populates="items")