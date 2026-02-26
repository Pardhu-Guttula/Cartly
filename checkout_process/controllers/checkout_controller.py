# Epic Title: Integrate multiple payment gateways

from flask import Blueprint, request, jsonify
from checkout_process.services.payment_gateway_service import PaymentGatewayService
from checkout_process.models.transaction import Transaction
from backend import db

checkout_bp = Blueprint('checkout', __name__)
payment_service = PaymentGatewayService()

@checkout_bp.route('/checkout', methods=['POST'])
def process_checkout():
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    payment_gateway = data.get('payment_gateway')
    payment_details = data.get('payment_details')

    if not payment_details:
        return jsonify({"error": "Payment details are required"}), 400 

    if not payment_service.is_gateway_available(payment_gateway):
        return jsonify({"error": f"Payment gateway {payment_gateway} is unavailable"}), 400

    if not payment_service.validate_payment(payment_gateway, payment_details):
        return jsonify({"error": "Invalid payment details"}), 400

    transaction = Transaction(user_id=user_id, amount=amount, status='success', payment_gateway=payment_gateway)
    try:
        db.session.add(transaction)
        db.session.commit()
        return jsonify({"message": "Transaction processed successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500