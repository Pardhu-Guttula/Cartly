from pydantic import BaseModel

# Epic Title: Log and store transactions securely

class TransactionLogCreate(BaseModel):
    transaction_id: str
    order_id: int
    amount: float
    status: str
    payment_gateway: str

class TransactionLogOut(BaseModel):
    id: int
    transaction_id: str
    order_id: int
    amount: float
    status: str
    payment_gateway: str
    created_at: str

    class Config:
        orm_mode = True