# Epic Title: Integrate Promotion System with Payment System

from flask import Blueprint, request, jsonify
from backend import db
from product_promotions_and_discounts.models.promotion import Promotion
from checkout_process.models.transaction import Transaction

promotion_bp = Blueprint('promotion', __name__)

@promotion_bp.route('/apply_promotion', methods=['POST'])
def apply_promotion():
    data = request.get_json()
    promotion_code = data.get('promotion_code')
    order_total = data.get('order_total')

    promotion = Promotion.query.filter_by(code=promotion_code).first()

    if not promotion:
        return jsonify({"error": "Invalid promotion code"}), 400

    if not promotion.is_valid():
        return jsonify({"error": "Promotion code is expired or inactive"}), 400

    discounted_amount = order_total - promotion.discount_amount
    if discounted_amount < 0:
        discounted_amount = 0

    return jsonify({
        "message": "Promotion applied successfully",
        "discounted_amount": discounted_amount,
        "promotion_code": promotion_code
    }), 200