# Epic Title: User Signup Functionality

from backend import db
from backend.models.credentials import Credentials
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    credentials_id = Column(Integer, db.ForeignKey('credentials.id'), nullable=False)

    credentials = relationship("Credentials", back_populates="user")

    def __init__(self, email: str, credentials: Credentials):
        self.email = email
        self.credentials = credentials