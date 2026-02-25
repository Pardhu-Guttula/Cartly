from fastapi import FastAPI
from backend.routes import promotion
from backend.services.database import init_db

# Epic Title: Apply Promotions During Checkout

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the routes
app.include_router(promotion.router, prefix="/api", tags=["Promotion"])