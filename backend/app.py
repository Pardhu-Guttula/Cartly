from fastapi import FastAPI
from backend.routes import router
from backend.services.database import initialize_database

# Epic Title: Develop PostgreSQL Database for Performance Metrics

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    initialize_database()

# Include the routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Performance Metrics and User Behavior API"}

### Database Schema