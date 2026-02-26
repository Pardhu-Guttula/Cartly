# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import admin_dashboard_bp

@admin_dashboard_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Admin Dashboard API is healthy'})