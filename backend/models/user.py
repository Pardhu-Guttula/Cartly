# Epic Title: Edit User Address

from backend import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    addresses = relationship("Address", back_populates="user")

    def __init__(self, username: str):
        self.username = username