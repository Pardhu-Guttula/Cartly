from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.user import Base  # Epic Title: User Signup Functionality

engine = create_engine('mysql://username:password@localhost/mydatabase')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)