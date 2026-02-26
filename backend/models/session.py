# Epic Title: User Login Functionality

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend import db
from backend.models.user import User

class Session(db.Model):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    jwt_token = Column(String(512), nullable=False)

    user = relationship('User', back_populates='sessions')

    def __init__(self, user: User, jwt_token: str):
        self.user = user
        self.jwt_token = jwt_token