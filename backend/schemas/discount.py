from pydantic import BaseModel

# Epic Title: Store Promotion and Discount Data in PostgreSQL

class DiscountCreate(BaseModel):
    discount_amount: float
    promotion_id: int

class DiscountOut(BaseModel):
    id: int
    discount_amount: float
    promotion_id: int

    class Config:
        orm_mode = True