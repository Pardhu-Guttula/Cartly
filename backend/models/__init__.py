from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.product import Base
from backend.models.category import Base
from backend.models.cart import Base
from backend.models.cart_item import Base
from backend.models.wishlist import Base
from backend.models.wishlist_item import Base

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

engine = create_engine('postgresql+psycopg2://username:password@localhost/mydatabase')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    import backend.models.product
    import backend.models.category
    import backend.models.cart
    import backend.models.cart_item
    import backend.models.wishlist
    import backend.models.wishlist_item
    Base.metadata.create_all(bind=engine)