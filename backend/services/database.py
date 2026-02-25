from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.models import Base

# Epic Title: Implement Efficient Product Search Functionality

engine = create_engine('mysql+mysqlconnector://username:password@localhost/mydatabase')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    import backend.models.product
    import backend.models.category
    Base.metadata.create_all(bind=engine)