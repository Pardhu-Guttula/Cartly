from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.models.user import Base as UserBase
from backend.models.address import Base as AddressBase

# Epic Title: Save User Address

DATABASE_URL = 'mysql+mysqlconnector://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_factory = scoped_session(SessionLocal)

def init_db():
    UserBase.metadata.create_all(bind=engine)
    AddressBase.metadata.create_all(bind=engine)