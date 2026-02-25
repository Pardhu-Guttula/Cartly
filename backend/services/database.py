from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from backend.models import Base

# Epic Title: Retrieve User Addresses

DATABASE_URL = 'mysql+mysqlconnector://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_factory = scoped_session(SessionLocal)

def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()

def init_db():
    import backend.models.user
    import backend.models.address
    Base.metadata.create_all(bind=engine)