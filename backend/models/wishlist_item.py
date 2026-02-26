# Epic Title: Implement Shopping Cart and Wishlist Functionality

from backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

class WishlistItem(db.Model):
    __tablename__ = 'wishlist_items'

    id = Column(Integer, primary_key=True)
    wishlist_id = Column(Integer, ForeignKey('wishlists.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)

    wishlist = relationship("Wishlist", back_populates="wishlist_items")
    product = relationship("Product")

    def __init__(self, wishlist_id: int, product_id: int):
        self.wishlist_id = wishlist_id
        self.product_id = product_id