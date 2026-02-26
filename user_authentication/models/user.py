# Epic Title: User Login Functionality

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
        # Securely store the password hash instead of plain text
        self.password = generate_password_hash(password)