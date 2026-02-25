from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Epic Title: Develop PostgreSQL Database for Performance Metrics

Base = declarative_base()

class UserBehavior(Base):
    __tablename__ = 'user_behavior'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, nullable=False)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)