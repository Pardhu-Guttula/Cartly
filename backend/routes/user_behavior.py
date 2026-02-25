from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models.user_behavior import UserBehavior
from backend.services.database import get_db

# Epic Title: Develop PostgreSQL Database for Performance Metrics

router = APIRouter()

@router.post("/user_behavior")
def create_user_behavior(user_id: str, action: str, timestamp: str, db: Session = Depends(get_db)):
    try:
        behavior = UserBehavior(user_id=user_id, action=action, timestamp=timestamp)
        db.add(behavior)
        db.commit()
        db.refresh(behavior)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create user behavior record")

    return behavior

@router.get("/user_behavior")
def get_user_behavior(db: Session = Depends(get_db)):
    return db.query(UserBehavior).all()