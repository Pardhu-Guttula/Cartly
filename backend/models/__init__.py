from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from backend.models.transaction_log import Base

# Epic Title: Log and store transactions securely

DATABASE_URL = 'postgresql+psycopg2://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_factory = scoped_session(SessionLocal)

def init_db():
    import backend.models.transaction_log
    Base.metadata.create_all(bind=engine)