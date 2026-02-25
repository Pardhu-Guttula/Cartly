from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.product import Base
from backend.models.category import Base
from backend.models.cart import Base
from backend.models.cart_item import Base

# Epic Title: Implement Shopping Cart and Wishlist Functionality

engine = create_engine('mysql+mysqlconnector://username:password@localhost/mydatabase')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    import backend.models.product
    import backend.models.category
    import backend.models.cart
    import backend.models.cart_item
    Base.metadata.create_all(bind=engine)