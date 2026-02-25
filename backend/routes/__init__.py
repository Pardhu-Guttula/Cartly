from fastapi import APIRouter
from backend.routes import promotion

# Epic Title: Develop Frontend Interface for Promotions

router = APIRouter()
router.include_router(promotion.router, prefix="/api/promotions", tags=["promotions"])