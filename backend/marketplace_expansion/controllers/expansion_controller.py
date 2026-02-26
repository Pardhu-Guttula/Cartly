# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import marketplace_expansion_bp

@marketplace_expansion_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Marketplace Expansion API is healthy'})