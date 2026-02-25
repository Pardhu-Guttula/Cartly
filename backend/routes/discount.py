from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models.discount import Discount
from backend.schemas.discount import DiscountCreate, DiscountOut
from backend.services.database import get_db

# Epic Title: Store Promotion and Discount Data in PostgreSQL

router = APIRouter()

@router.post("/discount", response_model=DiscountOut)
def create_discount(discount_create: DiscountCreate, db: Session = Depends(get_db)):
    discount = Discount(**discount_create.dict())
    try:
        db.add(discount)
        db.commit()
        db.refresh(discount)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create discount")

    return discount

@router.get("/discount/{discount_id}", response_model=DiscountOut)
def get_discount(discount_id: int, db: Session = Depends(get_db)):
    discount = db.query(Discount).filter(Discount.id == discount_id).first()
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount