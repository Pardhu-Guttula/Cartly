from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.product import Base

# Epic Title: Integrate dashboard with PostgreSQL

DATABASE_URL = 'postgresql+psycopg2://username:password@localhost/mydatabase'

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    import backend.models.product
    Base.metadata.create_all(bind=engine)