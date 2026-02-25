from fastapi import FastAPI
from backend.routes import wishlist
from backend.services.database import init_db

# Epic Title: Implement Shopping Cart and Wishlist Functionality

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the wishlist routes
app.include_router(wishlist.router, prefix="/api/wishlist", tags=["Wishlist"])