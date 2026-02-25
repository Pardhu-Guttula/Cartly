from fastapi import FastAPI
from backend.routes import product_browsing
from backend.services.database import init_db

# Epic Title: Develop Reusable Product Browsing Components

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the product browsing route
app.include_router(product_browsing.router, prefix="/api/products", tags=["Product Browsing"])