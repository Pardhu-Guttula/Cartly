from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.models.promotion import Base as PromotionBase
from backend.models.transaction import Base as TransactionBase

# Epic Title: Integrate Promotion System with Payment System

DATABASE_URL = 'mysql+mysqlconnector://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_factory = scoped_session(SessionLocal)

def init_db():
    PromotionBase.metadata.create_all(bind=engine)
    TransactionBase.metadata.create_all(bind=engine)