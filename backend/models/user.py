from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: User Signup Functionality

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)