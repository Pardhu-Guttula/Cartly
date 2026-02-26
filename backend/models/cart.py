# Epic Title: Implement Shopping Cart and Wishlist Functionality

from backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

class Cart(db.Model):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    total_price = Column(db.Numeric(10, 2), nullable=False, default=0.0)

    cart_items = relationship("CartItem", back_populates="cart")

    def __init__(self, user_id: int, total_price: float = 0.0):
        self.user_id = user_id
        self.total_price = total_price