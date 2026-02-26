# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import user_accounts_bp

@user_accounts_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'User Accounts API is healthy'})