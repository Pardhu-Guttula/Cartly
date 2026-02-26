# Epic Title: User Password Security

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from backend.models.user import User
from backend.models.credentials import Credentials
from backend import db

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already in use"}), 400
    
    # Validate password complexity (e.g., minimum length)
    if len(password) < 8:
        return jsonify({"error": "Password does not meet the requirements"}), 400

    hashed_password = generate_password_hash(password)
    credentials = Credentials(password=hashed_password)
    user = User(email=email, credentials=credentials)
    
    db.session.add(credentials)
    db.session.add(user)
    db.session.commit()
    
    # Here we should send a confirmation email (not implemented)
    
    return jsonify({"message": "User created successfully"}), 201