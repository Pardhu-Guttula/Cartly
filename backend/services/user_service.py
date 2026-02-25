from backend.models import SessionLocal
from backend.models.user import User
from backend.schemas.user import UserCreateSchema
import logging

# Epic Title: User Signup Functionality

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:
    
    @staticmethod
    def create_user(user_data: UserCreateSchema):
        session = SessionLocal()
        try:
            user = User(email=user_data.email, password=user_data.password)
            session.add(user)
            session.commit()
            logger.info(f"User created with email: {user.email}")
            return user
        except Exception as e:
            session.rollback()
            logger.error(f"Error creating user: {e}")
            raise
        finally:
            session.close()
    
    @staticmethod
    def is_email_unique(email: str) -> bool:
        session = SessionLocal()
        try:
            user = session.query(User).filter(User.email == email).first()
            return user is None
        except Exception as e:
            session.rollback()
            logger.error(f"Error checking email uniqueness: {e}")
            raise
        finally:
            session.close()