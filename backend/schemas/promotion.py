from pydantic import BaseModel

# Epic Title: Apply Promotions During Checkout

class PromotionApply(BaseModel):
    code: str

class PromotionResult(BaseModel):
    code: str
    description: str
    discount_amount: float

    class Config:
        orm_mode = True