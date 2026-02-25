from pydantic import BaseModel

# Epic Title: Implement product management functionality

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    inventory: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True