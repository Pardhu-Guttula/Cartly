from fastapi import FastAPI
from backend.routes import product_search
from backend.services.database import init_db

# Epic Title: Implement Efficient Product Search Functionality

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the product search route
app.include_router(product_search.router, prefix="/api/products", tags=["Product Search"])