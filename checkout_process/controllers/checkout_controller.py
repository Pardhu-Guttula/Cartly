# Epic Title: Apply Promotions During Checkout

from flask import Blueprint, request, jsonify
from backend import db
from product_promotions_and_discounts.models.promotion import Promotion

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/apply_promotion', methods=['POST'])
def apply_promotion():
    data = request.get_json()
    promotion_code = data.get('promotion_code')

    promotion = Promotion.query.filter_by(code=promotion_code).first()

    if not promotion:
        return jsonify({"error": "Invalid promotion code"}), 400

    if not promotion.is_valid():
        return jsonify({"error": "Promotion code is expired or inactive"}), 400

    return jsonify({
        "message": "Promotion applied successfully",
        "discount_amount": promotion.discount_amount
    }), 200