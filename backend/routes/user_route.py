from flask import Blueprint, request, jsonify
from backend.schemas.user import UserCreateSchema
from backend.services.user_service import UserService
import logging

# Epic Title: User Signup Functionality

logger = logging.getLogger(__name__)
user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    try:
        user_data = UserCreateSchema(**request.json)
        if not UserService.is_email_unique(user_data.email):
            return jsonify({"error": "Email is already in use"}), 400
        UserService.create_user(user_data)
        return jsonify({"message": "User created successfully"}), 201
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        return jsonify({"error": "Invalid input"}), 400
    except Exception as e:
        logger.error(f"Error in signup endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500