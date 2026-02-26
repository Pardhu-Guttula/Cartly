# Epic Title: Implement shopping cart and wishlist functionality

from backend import db
from sqlalchemy import Column, Integer, Float, ForeignKey

class ShoppingCartItem(db.Model):
    __tablename__ = 'shopping_cart_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    cart_id = Column(Integer, ForeignKey('shopping_carts.id', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False)

    shopping_cart = db.relationship("ShoppingCart", back_populates="items")
    product = db.relationship("Product")

    def __init__(self, product_id: int, cart_id: int, quantity: int, price: float):
        self.product_id = product_id
        self.cart_id = cart_id
        self.quantity = quantity
        self.price = price