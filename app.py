from fastapi import FastAPI
from backend.routes import cart
from backend.services.database import init_db

# Epic Title: Implement Shopping Cart and Wishlist Functionality

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the cart routes
app.include_router(cart.router, prefix="/api/cart", tags=["Cart"])