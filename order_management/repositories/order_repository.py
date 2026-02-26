# Epic Title: Integrate Promotion System with Order Management

from backend import db
from order_management.models.order import Order

class OrderRepository:

    @staticmethod
    def add_order(order: Order) -> None:
        db.session.add(order)
        db.session.commit()

    @staticmethod
    def get_order_by_id(order_id: int) -> Order:
        return Order.query.get(order_id)

    @staticmethod
    def update_order(order: Order) -> None:
        db.session.commit()