from fastapi import FastAPI
from backend.routes import router
from backend.services.database import init_db

# Epic Title: Develop Frontend Interface for Promotions

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the routes
app.include_router(router)