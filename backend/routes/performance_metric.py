from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models.performance_metric import PerformanceMetric
from backend.services.database import get_db

# Epic Title: Develop PostgreSQL Database for Performance Metrics

router = APIRouter()

@router.post("/performance_metrics")
def create_performance_metric(metric_name: str, value: float, timestamp: str, db: Session = Depends(get_db)):
    try:
        metric = PerformanceMetric(metric_name=metric_name, value=value, timestamp=timestamp)
        db.add(metric)
        db.commit()
        db.refresh(metric)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create performance metric")

    return metric

@router.get("/performance_metrics")
def get_performance_metrics(db: Session = Depends(get_db)):
    return db.query(PerformanceMetric).all()