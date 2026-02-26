# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import analytics_reporting_bp

@analytics_reporting_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Analytics and Reporting API is healthy'})