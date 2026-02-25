from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models import Address, User
from backend.schemas import AddressCreate, AddressOut
from backend.services.database import get_db

# Epic Title: Save User Address

router = APIRouter()

@router.post("/address", response_model=AddressOut)
def save_address(address_details: AddressCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if not address_details.street or not address_details.city or not address_details.postal_code:
        raise HTTPException(status_code=400, detail="Mandatory fields are missing")
    
    if not validate_postal_code(address_details.postal_code):
        raise HTTPException(status_code=400, detail="Invalid postal code")
    
    encrypted_address = Address.encrypt_address(
        f"{address_details.street}, {address_details.city}, {address_details.state}, {address_details.postal_code}")
    
    new_address = Address(
        user_id=user.id,
        encrypted_address=encrypted_address
    )
    
    try:
        db.add(new_address)
        db.commit()
        db.refresh(new_address)
        return AddressOut(
            id=new_address.id,
            street=address_details.street,
            city=address_details.city,
            state=address_details.state,
            postal_code=address_details.postal_code
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to save address")

def get_current_user():
    # Placeholder for user authentication
    return User(id=1, username="dummy_user")

def validate_postal_code(postal_code: str) -> bool:
    # Placeholder for validating postal code
    return len(postal_code) == 5