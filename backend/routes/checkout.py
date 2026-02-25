from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models.promotion import Promotion
from backend.models.transaction import Transaction
from backend.schemas.checkout import CheckoutRequest, CheckoutResponse
from backend.services.database import get_db
from datetime import datetime

# Epic Title: Integrate Promotion System with Payment System

router = APIRouter()

@router.post("/checkout", response_model=CheckoutResponse)
def checkout_process(checkout_request: CheckoutRequest, db: Session = Depends(get_db)):
    promotion = db.query(Promotion).filter(Promotion.code == checkout_request.promo_code).first()

    final_amount = checkout_request.amount
    discount_amount = 0.0

    if promotion:
        if promotion.is_valid():
            discount_amount = promotion.discount_amount
            final_amount -= discount_amount
        else:
            raise HTTPException(status_code=400, detail="Promotion has expired")

    transaction = Transaction(
        amount=checkout_request.amount,
        discount=discount_amount,
        final_amount=final_amount,
        promo_code=checkout_request.promo_code,
        promotion_id=promotion.id if promotion else None,
        status="pending"
    )

    try:
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to process transaction")

    # Here we would integrate with an actual payment system
    # simulate_payment = pay_with_external_service(transaction.final_amount)

    # For the sake of this example, we'll assume success:
    simulate_payment_success = True
    
    if simulate_payment_success:
        transaction.status = "completed"
        db.commit()
    else:
        transaction.status = "failed"
        db.commit()
        raise HTTPException(status_code=500, detail="Payment failed, promotion rolled back")

    return CheckoutResponse(
        transaction_id=transaction.id,
        amount=transaction.amount,
        discount=transaction.discount,
        final_amount=transaction.final_amount,
        status=transaction.status
    )