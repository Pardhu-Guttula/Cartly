from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models import TransactionLog
from backend.schemas import TransactionLogCreate, TransactionLogOut
from backend.services.database import get_db
import logging

# Epic Title: Log and store transactions securely

router = APIRouter()

@router.post("/log", response_model=TransactionLogOut)
def log_transaction(transaction_log: TransactionLogCreate, db: Session = Depends(get_db)):
    new_transaction_log = TransactionLog(**transaction_log.dict())
    try:
        db.add(new_transaction_log)
        db.commit()
        db.refresh(new_transaction_log)
        return new_transaction_log
    except Exception as e:
        logging.error(f"Failed to log transaction: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to log transaction")

@router.get("/logs", response_model=list[TransactionLogOut])
def get_transaction_logs(db: Session = Depends(get_db)):
    logs = db.query(TransactionLog).all()
    return logs