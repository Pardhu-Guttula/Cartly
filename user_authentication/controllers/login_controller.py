# Epic Title: User Login Functionality

from flask import Blueprint, request, jsonify
from user_authentication.services.login_service import LoginService

login_bp = Blueprint('login_controller', __name__)
login_service = LoginService()

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    result = login_service.authenticate_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Login successful', 'token': result['token']}), 200