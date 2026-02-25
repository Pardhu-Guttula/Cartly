from pydantic import BaseModel

# Epic Title: Integrate multiple payment gateways

class PaymentDetails(BaseModel):
    card_number: str
    expiry_date: str
    cvv: str

class CheckoutCreate(BaseModel):
    order_id: int
    amount: float
    payment_gateway: str
    payment_details: PaymentDetails

class TransactionOut(BaseModel):
    id: int
    order_id: int
    amount: float
    status: str
    payment_gateway: str
    created_at: str

    class Config:
        orm_mode = True

class PaymentGatewayOut(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        orm_mode = True