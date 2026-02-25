from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.user import Base

# Epic Title: User Login Functionality

class Session(Base):
    __tablename__ = 'sessions'
    
    id = Column(Integer, Sequence('session_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    jwt_token = Column(String(255), nullable=False)

    user = relationship("User", back_populates="sessions")