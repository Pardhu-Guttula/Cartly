# Epic Title: Implement Shopping Cart and Wishlist Functionality

from backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    cart = relationship("Cart", back_populates="cart_items")
    product = relationship("Product")

    def __init__(self, cart_id: int, product_id: int, quantity: int = 1):
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity