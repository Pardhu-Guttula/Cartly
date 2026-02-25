from fastapi import FastAPI
from backend.routes import checkout
from backend.services.database import init_db

# Epic Title: Integrate Promotion System with Payment System

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the routes
app.include_router(checkout.router, prefix="/api", tags=["Checkout"])