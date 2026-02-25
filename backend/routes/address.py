from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models import Address, User
from backend.schemas import AddressCreate, AddressOut
from backend.services.database import get_db

# Epic Title: Edit User Address

router = APIRouter()

@router.put("/address/{address_id}", response_model=AddressOut)
def update_address(address_id: int, address_details: AddressCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    existing_address = db.query(Address).filter(Address.id == address_id, Address.user_id == user.id).first()
    if not existing_address:
        raise HTTPException(status_code=404, detail="Address not found")

    if not address_details.street or not address_details.city or not address_details.postal_code:
        raise HTTPException(status_code=400, detail="Mandatory fields are missing")
    
    if not validate_postal_code(address_details.postal_code):
        raise HTTPException(status_code=400, detail="Invalid postal code")
    
    updated_address = existing_address.encrypt_address(
        f"{address_details.street}, {address_details.city}, {address_details.state}, {address_details.postal_code}")

    existing_address.encrypted_address = updated_address
    
    try:
        db.commit()
        db.refresh(existing_address)
        return AddressOut(
            id=existing_address.id,
            street=address_details.street,
            city=address_details.city,
            state=address_details.state,
            postal_code=address_details.postal_code
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update address")

def get_current_user():
    # Placeholder for user authentication
    return User(id=1, username="dummy_user")

def validate_postal_code(postal_code: str) -> bool:
    # Placeholder for validating postal code
    return len(postal_code) == 5