# Epic Title: User Password Security

from backend import db
from user_authentication.models.user import User

class UserRepository:

    def find_by_email(self, email: str):
        return User.query.filter_by(email=email).first()

    def save(self, user: User):
        db.session.add(user)
        db.session.commit()