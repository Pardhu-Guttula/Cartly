from pydantic import BaseModel

# Epic Title: Edit User Address

class AddressCreate(BaseModel):
    street: str
    city: str
    state: str
    postal_code: str

class AddressOut(BaseModel):
    id: int
    street: str
    city: str
    state: str
    postal_code: str

    class Config:
        orm_mode = True