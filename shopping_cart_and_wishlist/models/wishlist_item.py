# Epic Title: Implement shopping cart and wishlist functionality

from backend import db
from sqlalchemy import Column, Integer, ForeignKey

class WishlistItem(db.Model):
    __tablename__ = 'wishlist_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    wishlist_id = Column(Integer, ForeignKey('wishlists.id', ondelete='CASCADE'), nullable=False)

    wishlist = db.relationship('Wishlist', back_populates='items')
    product = db.relationship('Product')

    def __init__(self, product_id: int, wishlist_id: int):
        self.product_id = product_id
        self.wishlist_id = wishlist_id