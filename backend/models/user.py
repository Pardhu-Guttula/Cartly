from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: User Login Functionality

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    primary_mobile_number = Column(String(20), nullable=False)
    secondary_mobile_number = Column(String(20), nullable=True)

    sessions = relationship("Session", back_populates="user")

class Session(Base):
    __tablename__ = 'sessions'
    
    id = Column(Integer, Sequence('session_id_seq'), primary_key=True)
    user_id = Column(Integer, nullable=False)
    token = Column(String(500), nullable=False)

    user = relationship("User", back_populates="sessions")