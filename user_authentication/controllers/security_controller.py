# Epic Title: User Password Security

from flask import Blueprint, request, jsonify
from user_authentication.services.security_service import SecurityService

security_bp = Blueprint('security_controller', __name__)
security_service = SecurityService()

@security_bp.route('/change_password', methods=['POST'])
def change_password():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('new_password')

    if not email or not new_password:
        return jsonify({'message': 'Email and new password are required'}), 400

    result = security_service.update_password(email, new_password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Password updated successfully'}), 200