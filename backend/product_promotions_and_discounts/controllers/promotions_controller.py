# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import promotions_discounts_bp

@promotions_discounts_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Promotions and Discounts API is healthy'})