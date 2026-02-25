from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from backend.models import Transaction
from backend.schemas import CheckoutCreate, TransactionOut
from backend.services.database import get_db
import logging

# Epic Title: Implement secure checkout process

router = APIRouter()

@router.post("/checkout", response_model=TransactionOut)
def process_checkout(checkout_details: CheckoutCreate, db: Session = Depends(get_db)):
    if not checkout_details.payment_details:
        raise HTTPException(status_code=400, detail="Payment details are required")
    
    transaction = Transaction(
        order_id=checkout_details.order_id,
        amount=checkout_details.amount,
        status="successful"
    )
    try:
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction
    except Exception as e:
        logging.error(f"Failed to process transaction: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to process transaction")