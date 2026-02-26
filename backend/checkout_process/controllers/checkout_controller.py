# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import checkout_process_bp

@checkout_process_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Checkout Process API is healthy'})