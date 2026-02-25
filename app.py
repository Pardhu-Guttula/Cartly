from fastapi import FastAPI
from backend.routes import address
from backend.services.database import init_db

# Epic Title: Delete User Address

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the address routes
app.include_router(address.router, prefix="/api", tags=["Address"])