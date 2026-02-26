# Epic Title: Address Data Security

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from cryptography.fernet import Fernet
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
        self.street = self.encrypt_data(street)
        self.city = self.encrypt_data(city)
        self.state = self.encrypt_data(state)
        self.postal_code = self.encrypt_data(postal_code)
        self.country = self.encrypt_data(country)

    @staticmethod
    def encrypt_data(data: str) -> str:
        cipher_suite = Fernet(Address.get_encryption_key())
        return cipher_suite.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt_data(data: str) -> str:
        cipher_suite = Fernet(Address.get_encryption_key())
        return cipher_suite.decrypt(data.encode()).decode()

    @staticmethod
    def get_encryption_key() -> bytes:
        key = b'your-secret-key-goes-here'
        return key