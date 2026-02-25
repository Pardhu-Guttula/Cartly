from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models import Address, User
from backend.schemas import AddressCreate, AddressOut
from backend.services.database import get_db
import logging

# Epic Title: Address Data Security

router = APIRouter()

def get_current_user():
    # Placeholder for user authentication
    return User(id=1, username="dummy_user", is_authorized=True)

def ensure_authorized_user(user: User):
    if not user.is_authorized:
        logging.error(f"Unauthorized access attempt by user_id={user.id}")
        raise HTTPException(status_code=403, detail="Access denied")

@router.post("/address", response_model=AddressOut)
def save_address(address_details: AddressCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    ensure_authorized_user(user)
    
    if not address_details.street or not address_details.city or not address_details.postal_code:
        raise HTTPException(status_code=400, detail="Mandatory fields are missing")
    
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

@router.get("/address", response_model=list[AddressOut])
def get_addresses(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    ensure_authorized_user(user)

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