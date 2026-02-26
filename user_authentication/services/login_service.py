# Epic Title: User Login Functionality

from datetime import datetime, timedelta
import jwt
from werkzeug.security import check_password_hash
from user_authentication.models.user import User
from user_authentication.repositories.user_repository import UserRepository

class LoginService:
    SECRET_KEY = "SECRET_KEY_PLACEHOLDER"  # In real applications, use environment variables

    def __init__(self):
        self.user_repository = UserRepository()

    def authenticate_user(self, email: str, password: str) -> dict:
        user = self.user_repository.find_by_email(email)
        if not user or not check_password_hash(user.password, password):
            return {'status': 'error', 'message': 'Invalid login credentials'}

        token = self.generate_jwt(user.email)

        return {'status': 'success', 'token': token}

    def generate_jwt(self, email: str) -> str:
        payload = {
            'exp': datetime.utcnow() + timedelta(hours=1),
            'iat': datetime.utcnow(),
            'sub': email
        }
        return jwt.encode(payload, self.SECRET_KEY, algorithm='HS256')