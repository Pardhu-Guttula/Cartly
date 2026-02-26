# Epic Title: Store Promotion and Discount Data in PostgreSQL

from product_promotions_and_discounts.repositories.promotion_repository import PromotionRepository
from product_promotions_and_discounts.models.promotion import Promotion
from datetime import datetime

class PromotionService:

    @staticmethod
    def create_promotion(code: str, discount_amount: int, expiry_date: datetime) -> None:
        promotion = Promotion(code=code, discount_amount=discount_amount, expiry_date=expiry_date)
        PromotionRepository.add_promotion(promotion)

    @staticmethod
    def update_promotion(code: str, discount_amount: int, expiry_date: datetime, active: bool) -> None:
        promotion = PromotionRepository.get_promotion_by_code(code)
        if promotion:
            promotion.discount_amount = discount_amount
            promotion.expiry_date = expiry_date
            promotion.active = active
            PromotionRepository.update_promotion(promotion)

    @staticmethod
    def get_promotion(code: str) -> Promotion:
        return PromotionRepository.get_promotion_by_code(code)

    @staticmethod
    def list_promotions() -> list[Promotion]:
        return PromotionRepository.get_all_promotions()