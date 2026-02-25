from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from backend.models import init_db

# Epic Title: Develop PostgreSQL Database for Performance Metrics

DATABASE_URL = 'postgresql+psycopg2://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session_factory = scoped_session(SessionLocal)

def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()

def initialize_database():
    init_db()

### Routes