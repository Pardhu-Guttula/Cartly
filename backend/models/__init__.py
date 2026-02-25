from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.product import Base
from backend.models.category import Base

# Epic Title: Ensure Data Integrity and Referential Integrity in Product-Category Models

engine = create_engine('postgresql://username:password@localhost/mydatabase')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    import backend.models.product
    import backend.models.category
    Base.metadata.create_all(bind=engine)