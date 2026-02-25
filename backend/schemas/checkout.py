from pydantic import BaseModel

# Epic Title: Integrate Promotion System with Payment System

class CheckoutRequest(BaseModel):
    amount: float
    promo_code: str

class CheckoutResponse(BaseModel):
    transaction_id: int
    amount: float
    discount: float
    final_amount: float
    status: str

    class Config:
        orm_mode = True