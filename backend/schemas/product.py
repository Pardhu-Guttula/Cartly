from pydantic import BaseModel

# Epic Title: Develop Reusable Product Browsing Components

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    rating: float
    category_id: int
    inventory: int

    class Config:
        orm_mode = True

class ProductPage(BaseModel):
    products: list[Product]
    total: int
    page: int
    page_size: int