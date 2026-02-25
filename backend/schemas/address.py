from pydantic import BaseModel

# Epic Title: Retrieve User Addresses

class AddressOut(BaseModel):
    id: int
    street: str
    city: str
    state: str
    postal_code: str

    class Config:
        orm_mode = True