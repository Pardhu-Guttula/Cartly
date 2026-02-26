# Epic Title: User Signup Functionality

import re
from user_authentication.models.user import User
from user_authentication.repositories.user_repository import UserRepository

class SignupService:

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, email: str, password: str) -> dict:
        if not self.is_valid_email(email):
            return {'status': 'error', 'message': 'Invalid email address'}

        if not self.is_valid_password(password):
            return {'status': 'error', 'message': 'Password does not meet complexity requirements'}

        existing_user = self.user_repository.find_by_email(email)
        if existing_user:
            return {'status': 'error', 'message': 'Email is already in use'}

        new_user = User(email=email, password=password)
        self.user_repository.save(new_user)

        # Placeholder for sending confirmation email logic

        return {'status': 'success'}

    def is_valid_email(self, email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def is_valid_password(self, password: str) -> bool:
        return len(password) >= 8