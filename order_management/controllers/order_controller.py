# Epic Title: Integrate Promotion System with Order Management

from flask import Blueprint, request, jsonify
from backend import db
from order_management.models.order import Order
from product_promotions_and_discounts.models.promotion import Promotion
import logging

order_bp = Blueprint('order', __name__)

@order_bp.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    total_amount = data.get('total_amount')
    promotion_code = data.get('promotion_code')

    final_amount = total_amount
    if promotion_code:
        promotion = Promotion.query.filter_by(code=promotion_code).first()
        if promotion and promotion.is_valid():
            final_amount = total_amount - promotion.discount_amount
            if final_amount < 0:
                final_amount = 0
        else:
            logging.error(f"Invalid or expired promotion code: {promotion_code}")
            return jsonify({"error": "Invalid or expired promotion code"}), 400

    order = Order(user_id=user_id, total_amount=total_amount, promotion_code=promotion_code, final_amount=final_amount)
    try:
        db.session.add(order)
        db.session.commit()
        return jsonify({"message": "Order created successfully", "order_id": order.id}), 201
    except Exception as e:
        db.session.rollback()
        logging.error(f"Order creation failed: {str(e)}")
        return jsonify({"error": "Order creation failed"}), 500