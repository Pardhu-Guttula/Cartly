from fastapi import FastAPI
from backend.routes import product
from backend.services.database import init_db

# Epic Title: Integrate dashboard with PostgreSQL

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the product routes
app.include_router(product.router, prefix="/api/products", tags=["Products"])