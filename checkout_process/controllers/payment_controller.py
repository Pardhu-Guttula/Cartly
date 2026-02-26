# Epic Title: Integrate Promotion System with Payment System

from flask import Blueprint, request, jsonify
from backend import db
from product_promotions_and_discounts.models.promotion import Promotion
from checkout_process.models.transaction import Transaction

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    order_total = data.get('order_total')
    promotion_code = data.get('promotion_code')

    if promotion_code:
        promotion = Promotion.query.filter_by(code=promotion_code).first()
        if not promotion:
            return jsonify({"error": "Invalid promotion code"}), 400

        if not promotion.is_valid():
            return jsonify({"error": "Promotion code is expired or inactive"}), 400

        discounted_amount = order_total - promotion.discount_amount
        if discounted_amount < 0:
            discounted_amount = 0
    else:
        discounted_amount = order_total

    transaction = Transaction(amount=discounted_amount, promotion_code=promotion_code)
    try:
        db.session.add(transaction)
        db.session.commit()
        return jsonify({"message": "Payment processed successfully", "transaction_id": transaction.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Payment processing failed", "details": str(e)}), 500