# Epic Title: Integrate Promotion System with Order Management

from order_management.models.order import Order
from product_promotions_and_discounts.models.promotion import Promotion
from order_management.repositories.order_repository import OrderRepository

class OrderService:

    @staticmethod
    def update_promotion(order_id: int, promotion_code: str) -> None:
        order = OrderRepository.get_order_by_id(order_id)
        if not order:
            raise ValueError("Order not found")

        promotion = Promotion.query.filter_by(code=promotion_code).first()

        if not promotion or not promotion.is_valid():
            raise ValueError("Invalid or expired promotion code")

        order.promotion_code = promotion_code
        order.final_amount = order.total_amount - promotion.discount_amount
        if order.final_amount < 0:
            order.final_amount = 0
        
        OrderRepository.update_order(order)