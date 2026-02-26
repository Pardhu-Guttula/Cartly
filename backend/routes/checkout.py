# Epic Title: Integrate Multiple Payment Gateways

from flask import Blueprint, request, jsonify
from backend.models.transaction import Transaction
from backend import db

checkout_bp = Blueprint('checkout', __name__)

# List of available payment gateways
PAYMENT_GATEWAYS = ["Gateway1", "Gateway2", "Gateway3"]

@checkout_bp.route('/checkout', methods=['POST'])
def process_payment():
    data = request.get_json()
    payment_details = data.get('payment_details')
    amount = data.get('amount')
    payment_gateway = data.get('payment_gateway')
    
    if payment_gateway not in PAYMENT_GATEWAYS:
        return jsonify({'message': 'Selected payment gateway is unavailable'}), 400

    # Dummy validation and transaction processing
    if not payment_details:
        return jsonify({'message': 'Payment details are required'}), 400

    if payment_details == "invalid":
        return jsonify({'message': 'Payment failed'}), 400

    new_transaction = Transaction(amount=amount, status='Success', payment_gateway=payment_gateway)
    db.session.add(new_transaction)
    db.session.commit()

    return jsonify({'message': 'Transaction completed successfully'})