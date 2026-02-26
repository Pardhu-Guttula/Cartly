# Epic Title: Implement shopping cart and wishlist functionality

from backend import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Wishlist(db.Model):
    __tablename__ = 'wishlists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    user = relationship('User', back_populates='wishlist')
    items = relationship('WishlistItem', back_populates='wishlist', cascade='all, delete-orphan')

    def __init__(self, user_id: int):
        self.user_id = user_id