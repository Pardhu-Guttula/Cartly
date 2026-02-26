# Epic Title: User Login Functionality

from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta
from backend.models.user import User
from backend.models.session import Session
from backend import db

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user is None or not check_password_hash(user.credentials.password, password):
        return jsonify({"error": "Invalid login credentials"}), 401

    jwt_token = jwt.encode(
        {'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=1)},
        'your_jwt_secret_key',  # Replace with real secret key
        algorithm='HS256'
    )
    
    session = Session(user=user, jwt_token=jwt_token)
    db.session.add(session)
    db.session.commit()
    
    return jsonify({'token': jwt_token}), 200