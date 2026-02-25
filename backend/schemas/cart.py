from pydantic import BaseModel

# Epic Title: Implement Shopping Cart and Wishlist Functionality

class CartItem(BaseModel):
    id: int
    cart_id: int
    product_id: int
    quantity: int
    price_per_unit: float
    total_price: float

    class Config:
        orm_mode = True

class Cart(BaseModel):
    id: int
    user_id: int
    total_price: float
    items: list[CartItem]

    class Config:
        orm_mode = True

class CartUpdate(BaseModel):
    user_id: int
    product_id: int
    quantity: int