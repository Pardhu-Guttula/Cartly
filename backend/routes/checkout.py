from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from backend.models import Transaction, PaymentGateway
from backend.schemas import CheckoutCreate, PaymentGatewayOut, TransactionOut
from backend.services.database import get_db
import logging

# Epic Title: Integrate multiple payment gateways

router = APIRouter()

@router.get("/payment-gateways", response_model=list[PaymentGatewayOut])
def get_payment_gateways(db: Session = Depends(get_db)):
    gateways = db.query(PaymentGateway).all()
    return gateways

@router.post("/checkout", response_model=TransactionOut)
def process_checkout(checkout_details: CheckoutCreate, db: Session = Depends(get_db)):
    gateway = db.query(PaymentGateway).filter(PaymentGateway.name == checkout_details.payment_gateway).first()
    if gateway is None or gateway.status != "active":
        raise HTTPException(status_code=400, detail="Selected payment gateway is unavailable")
    
    transaction = Transaction(
        order_id=checkout_details.order_id,
        amount=checkout_details.amount,
        status="successful",
        payment_gateway=checkout_details.payment_gateway
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