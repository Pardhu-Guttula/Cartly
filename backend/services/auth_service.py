from backend.models import SessionLocal
from backend.models.user import User
from backend.models.session import Session
from backend.schemas.session import SessionSchema
import logging
import jwt
from datetime import datetime, timedelta

# Epic Title: User Login Functionality

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

class AuthService:
    
    @staticmethod
    def create_jwt(user_id: int) -> str:
        expiration = datetime.utcnow() + timedelta(hours=1)
        to_encode = {"sub": user_id, "exp": expiration}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def login(email: str, password: str):
        session = SessionLocal()
        try:
            user = session.query(User).filter(User.email == email).first()
            if user and user.password == password:
                jwt_token = AuthService.create_jwt(user.id)
                user_session = Session(user_id=user.id, jwt_token=jwt_token)
                session.add(user_session)
                session.commit()
                logger.info(f"User logged in with email: {email}")
                return SessionSchema(user_id=user.id, jwt_token=jwt_token)
            else:
                logger.warning(f"Invalid login attempt for email: {email}")
                raise ValueError("Invalid credentials")
        except Exception as e:
            session.rollback()
            logger.error(f"Error during login: {e}")
            raise
        finally:
            session.close()