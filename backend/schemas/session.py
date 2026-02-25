from pydantic import BaseModel

# Epic Title: User Login Functionality

class SessionSchema(BaseModel):
    user_id: int
    jwt_token: str