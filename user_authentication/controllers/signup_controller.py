# Epic Title: User Signup Functionality

from flask import Blueprint, request, jsonify
from user_authentication.services.signup_service import SignupService

signup_bp = Blueprint('signup_controller', __name__)
signup_service = SignupService()

@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    result = signup_service.create_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Account created successfully. Confirmation email sent.'}), 201