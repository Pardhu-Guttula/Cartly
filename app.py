from fastapi import FastAPI
from backend.routes import transaction_log
from backend.services.database import init_db

# Epic Title: Log and store transactions securely

app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    init_db()

# Include the transaction log routes
app.include_router(transaction_log.router, prefix="/api", tags=["Transaction Logs"])