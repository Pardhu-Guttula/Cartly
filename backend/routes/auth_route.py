from flask import Blueprint, request, jsonify
from backend.services.auth_service import AuthService
import logging

# Epic Title: User Login Functionality

logger = logging.getLogger(__name__)
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        result = AuthService.login(data['email'], data['password'])
        return jsonify(result.dict()), 200
    except ValueError as e:
        logger.error(f"Login validation error: {e}")
        return jsonify({"error": "Invalid login credentials"}), 400
    except Exception as e:
        logger.error(f"Error in login endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500