# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import user_authentication_bp

@user_authentication_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'User Authentication API is healthy'})