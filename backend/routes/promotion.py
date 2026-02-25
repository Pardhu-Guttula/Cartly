from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models.promotion import Promotion
from backend.models.discount import Discount
from backend.schemas.promotion import PromotionCreate, PromotionUpdate, PromotionOut
from backend.schemas.discount import DiscountCreate, DiscountOut
from backend.services.database import get_db

# Epic Title: Store Promotion and Discount Data in PostgreSQL

router = APIRouter()

@router.post("/promotion", response_model=PromotionOut)
def create_promotion(promotion_create: PromotionCreate, db: Session = Depends(get_db)):
    promotion = Promotion(**promotion_create.dict())
    try:
        db.add(promotion)
        db.commit()
        db.refresh(promotion)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create promotion")

    return promotion

@router.put("/promotion/{promotion_id}", response_model=PromotionOut)
def update_promotion(promotion_id: int, promotion_update: PromotionUpdate, db: Session = Depends(get_db)):
    promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    
    for var, value in vars(promotion_update).items():
        setattr(promotion, var, value) if value else None

    try:
        db.commit()
        db.refresh(promotion)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update promotion")

    return promotion

@router.get("/promotion/{promotion_id}", response_model=PromotionOut)
def get_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion