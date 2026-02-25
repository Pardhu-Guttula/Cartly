from pydantic import BaseModel

# Epic Title: Delete User Address

class AddressOut(BaseModel):
    id: int
    street: str
    city: str
    state: str
    postal_code: str

    class Config:
        orm_mode = True