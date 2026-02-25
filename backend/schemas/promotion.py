from pydantic import BaseModel
from datetime import date

# Epic Title: Store Promotion and Discount Data in PostgreSQL

class PromotionCreate(BaseModel):
    code: str
    description: str
    discount_amount: float
    expiration_date: date

class PromotionUpdate(BaseModel):
    code: str = None
    description: str = None
    discount_amount: float = None
    expiration_date: date = None

class PromotionOut(BaseModel):
    id: int
    code: str
    description: str
    discount_amount: float
    expiration_date: date

    class Config:
        orm_mode = True