from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from backend.models.promotion import Promotion
from backend.schemas.promotion import PromotionApply, PromotionResult
from backend.services.database import get_db

# Epic Title: Apply Promotions During Checkout

router = APIRouter()

@router.post("/promotion/apply", response_model=PromotionResult)
def apply_promotion(promotion_apply: PromotionApply, db: Session = Depends(get_db)):
    promotion = db.query(Promotion).filter(Promotion.code == promotion_apply.code).first()

    if not promotion:
        raise HTTPException(status_code=404, detail="Invalid promotion code")

    if not promotion.is_valid():
        raise HTTPException(status_code=400, detail="Promotion has expired")

    return PromotionResult(
        code=promotion.code,
        description=promotion.description,
        discount_amount=promotion.discount_amount
    )