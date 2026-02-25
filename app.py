from fastapi import FastAPI
from backend.routes import cart, wishlist
from backend.services.database import init_db

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the cart and wishlist routes
app.include_router(cart.router, prefix="/api/cart", tags=["Cart"])
app.include_router(wishlist.router, prefix="/api/wishlist", tags=["Wishlist"])