from pydantic import BaseModel

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

class WishlistItem(BaseModel):
    id: int
    wishlist_id: int
    product_id: int

    class Config:
        orm_mode = True

class Wishlist(BaseModel):
    id: int
    user_id: int
    items: list[WishlistItem]

    class Config:
        orm_mode = True