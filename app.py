from fastapi import FastAPI
from backend.routes import promotion, discount
from backend.services.database import init_db

# Epic Title: Store Promotion and Discount Data in PostgreSQL

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the routes
app.include_router(promotion.router, prefix="/api", tags=["Promotion"])
app.include_router(discount.router, prefix="/api", tags=["Discount"])