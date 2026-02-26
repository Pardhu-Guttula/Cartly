# Epic Title: Store Promotion and Discount Data in PostgreSQL

from backend import db
from product_promotions_and_discounts.models.promotion import Promotion

class PromotionRepository:

    @staticmethod
    def add_promotion(promotion: Promotion) -> None:
        db.session.add(promotion)
        db.session.commit()

    @staticmethod
    def update_promotion(promotion: Promotion) -> None:
        db.session.commit()

    @staticmethod
    def get_promotion_by_code(code: str) -> Promotion:
        return Promotion.query.filter_by(code=code).first()

    @staticmethod
    def get_all_promotions() -> list[Promotion]:
        return Promotion.query.all()