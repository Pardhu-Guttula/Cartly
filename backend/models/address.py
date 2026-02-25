from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from cryptography.fernet import Fernet
import os

# Epic Title: Save User Address

Base = declarative_base()
key = os.environ.get('ENCRYPTION_KEY', Fernet.generate_key())
cipher_suite = Fernet(key)

class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    encrypted_address = Column(String, nullable=False)
    user = relationship("User", back_populates="addresses")
    
    def encrypt_address(self, plain_text_address):
        return cipher_suite.encrypt(plain_text_address.encode()).decode()

    def decrypt_address(self):
        return cipher_suite.decrypt(self.encrypted_address.encode()).decode()