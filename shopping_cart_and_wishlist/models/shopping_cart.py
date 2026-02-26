# Epic Title: Implement shopping cart and wishlist functionality

from backend import db
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship

class ShoppingCart(db.Model):
    __tablename__ = 'shopping_carts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    total_price = Column(Float, nullable=False, default=0.0)

    user = relationship('User', back_populates='shopping_cart')
    items = relationship('ShoppingCartItem', back_populates='shopping_cart', cascade='all, delete-orphan')

    def __init__(self, user_id: int, total_price: float = 0.0):
        self.user_id = user_id
        self.total_price = total_price