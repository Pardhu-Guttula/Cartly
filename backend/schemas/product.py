from pydantic import BaseModel

# Epic Title: Implement Efficient Product Search Functionality

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int
    inventory: int

    class Config:
        orm_mode = True

class ProductSearchResults(BaseModel):
    products: list[Product]