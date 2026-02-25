from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: Implement Shopping Cart and Wishlist Functionality

Base = declarative_base()

class Cart(Base):
    __tablename__ = 'carts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, unique=True)
    total_price = Column(Float, nullable=False, default=0)

    items = relationship("CartItem", back_populates="cart")