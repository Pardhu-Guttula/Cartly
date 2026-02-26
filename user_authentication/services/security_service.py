# Epic Title: User Password Security

import re
from datetime import datetime, timedelta
from user_authentication.models.user import User
from user_authentication.repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

class SecurityService:

    def __init__(self):
        self.user_repository = UserRepository()
        self.login_attempts = {}

    def update_password(self, email: str, new_password: str) -> dict:
        if not self.is_valid_password(new_password):
            return {'status': 'error', 'message': 'Password does not meet complexity requirements'}

        user = self.user_repository.find_by_email(email)
        if not user:
            return {'status': 'error', 'message': 'User not found'}

        user.password = generate_password_hash(new_password)
        self.user_repository.save(user)
        return {'status': 'success'}

    def authenticate_user(self, email: str, password: str) -> dict:
        if self.is_account_locked(email):
            return {'status': 'error', 'message': 'Account is locked due to multiple failed login attempts'}

        user = self.user_repository.find_by_email(email)
        if not user or not check_password_hash(user.password, password):
            self.record_login_attempt(email)
            return {'status': 'error', 'message': 'Invalid login credentials'}
        
        return {'status': 'success'}

    def is_valid_password(self, password: str) -> bool:
        return len(password) >= 8

    def is_account_locked(self, email: str) -> bool:
        attempts_info = self.login_attempts.get(email)
        if not attempts_info:
            return False

        first_attempt_time, attempts = attempts_info
        if attempts >= 5 and datetime.now() - first_attempt_time < timedelta(minutes=1):
            return True
        
        if datetime.now() - first_attempt_time >= timedelta(minutes=1):
            self.login_attempts[email] = (datetime.now(), 0)

        return False

    def record_login_attempt(self, email: str):
        if email not in self.login_attempts:
            self.login_attempts[email] = (datetime.now(), 1)
        else:
            first_attempt_time, attempts = self.login_attempts[email]
            self.login_attempts[email] = (first_attempt_time, attempts + 1)