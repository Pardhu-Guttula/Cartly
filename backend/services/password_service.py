import bcrypt
import logging

# Epic Title: User Password Security

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PasswordService:

    @staticmethod
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        logger.info("Password hashed successfully")
        return hashed.decode()

    @staticmethod
    def check_password(hashed_password: str, plain_password: str) -> bool:
        matched = bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
        if matched:
            logger.info("Password matched successfully")
        else:
            logger.warning("Password did not match")
        return matched