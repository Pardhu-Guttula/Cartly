# Epic Title: Save User Address

from backend import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from cryptography.fernet import Fernet

key = Fernet.generate_key()  # In a real application, keep this key secure and persistent
cipher_suite = Fernet(key)

class Address(db.Model):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    address_line1 = Column(String(255), nullable=False)
    address_line2 = Column(String(255), nullable=True)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    encrypted_postal_code = Column(String(255), nullable=False)
    
    user = relationship("User", back_populates="addresses")

    def __init__(self, user_id: int, address_line1: str, address_line2: str, city: str, state: str, postal_code: str):
        self.user_id = user_id
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.encrypted_postal_code = cipher_suite.encrypt(postal_code.encode()).decode()