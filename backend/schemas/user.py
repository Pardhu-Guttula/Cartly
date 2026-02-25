from pydantic import BaseModel, EmailStr, constr

# Epic Title: User Signup Functionality

class UserCreateSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)