from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models import Address, User
from backend.schemas import AddressOut
from backend.services.database import get_db

# Epic Title: Retrieve User Addresses

router = APIRouter()

@router.get("/address", response_model=list[AddressOut])
def get_addresses(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    addresses = db.query(Address).filter(Address.user_id == user.id).all()
    if not addresses:
        return []

    return [
        AddressOut(
            id=address.id,
            street=address.decrypt_address().split(', ')[0],
            city=address.decrypt_address().split(', ')[1],
            state=address.decrypt_address().split(', ')[2],
            postal_code=address.decrypt_address().split(', ')[3]
        )
        for address in addresses
    ]

def get_current_user():
    # Placeholder for user authentication
    return User(id=1, username="dummy_user")