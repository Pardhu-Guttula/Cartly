from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

Base = declarative_base()

class CartItem(Base):
    __tablename__ = 'cart_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price_per_unit = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    
    cart = relationship("Cart", back_populates="items")