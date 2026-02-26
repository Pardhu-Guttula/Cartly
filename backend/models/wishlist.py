# Epic Title: Implement Shopping Cart and Wishlist Functionality

from backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer

class Wishlist(db.Model):
    __tablename__ = 'wishlists'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)

    wishlist_items = relationship("WishlistItem", back_populates="wishlist")

    def __init__(self, user_id: int):
        self.user_id = user_id