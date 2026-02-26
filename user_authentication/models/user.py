# Epic Title: User Password Security

from backend import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = generate_password_hash(password)