# Epic Title: Implement Secure Checkout Process

from flask import Blueprint, request, jsonify
from backend.models.transaction import Transaction
from backend import db

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/checkout', methods=['POST'])
def process_payment():
    data = request.get_json()
    payment_details = data.get('payment_details')
    amount = data.get('amount')

    # Dummy validation and transaction processing
    if not payment_details:
        return jsonify({'message': 'Payment details are required'}), 400

    if payment_details == "invalid":
        return jsonify({'message': 'Payment failed'}), 400

    new_transaction = Transaction(amount=amount, status='Success', payment_method='Credit Card')
    db.session.add(new_transaction)
    db.session.commit()

    return jsonify({'message': 'Transaction completed successfully'})