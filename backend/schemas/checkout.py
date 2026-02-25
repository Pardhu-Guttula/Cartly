from pydantic import BaseModel

# Epic Title: Implement secure checkout process

class PaymentDetails(BaseModel):
    card_number: str
    expiry_date: str
    cvv: str

class CheckoutCreate(BaseModel):
    order_id: int
    amount: float
    payment_details: PaymentDetails

class TransactionOut(BaseModel):
    id: int
    order_id: int
    amount: float
    status: str
    created_at: str

    class Config:
        orm_mode = True