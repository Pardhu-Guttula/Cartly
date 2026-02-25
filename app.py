from fastapi import FastAPI
from backend.routes import checkout
from backend.services.database import init_db

# Epic Title: Implement secure checkout process

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the checkout routes
app.include_router(checkout.router, prefix="/api", tags=["Checkout"])