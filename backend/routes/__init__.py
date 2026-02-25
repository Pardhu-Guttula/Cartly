from fastapi import APIRouter
from backend.routes import performance_metric, user_behavior

# Epic Title: Develop PostgreSQL Database for Performance Metrics

router = APIRouter()
router.include_router(performance_metric.router, prefix="/api", tags=["performance_metrics"])
router.include_router(user_behavior.router, prefix="/api", tags=["user_behavior"])

### Main Application