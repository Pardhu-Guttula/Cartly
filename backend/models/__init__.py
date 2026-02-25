from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.models.promotion import Base as PromotionBase
from backend.models.discount import Base as DiscountBase

# Epic Title: Develop Frontend Interface for Promotions

DATABASE_URL = 'mysql+mysqlconnector://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_factory = scoped_session(SessionLocal)

def init_db():
    PromotionBase.metadata.create_all(bind=engine)
    DiscountBase.metadata.create_all(bind=engine)