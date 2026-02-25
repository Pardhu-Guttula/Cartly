from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.models import Base

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

engine = create_engine('postgresql+psycopg2://username:password@localhost/mydatabase')
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
    import backend.models.cart
    import backend.models.cart_item
    import backend.models.wishlist
    import backend.models.wishlist_item
    Base.metadata.create_all(bind=engine)