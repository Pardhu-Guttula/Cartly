# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import mobile_optimization_bp

@mobile_optimization_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Mobile Optimization API is healthy'})