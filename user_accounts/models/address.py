# Epic Title: Retrieve User Addresses

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend import db

class Address(db.Model):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    street = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(100), nullable=False)

    user = relationship('User', backref=db.backref('addresses', lazy=True))

    def __init__(self, user_id: int, street: str, city: str, state: str, postal_code: str, country: str):
        self.user_id = user_id
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country