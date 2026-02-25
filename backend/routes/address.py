from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models import Address, User
from backend.schemas import AddressOut
from backend.services.database import get_db

# Epic Title: Delete User Address

router = APIRouter()

@router.delete("/address/{address_id}", response_model=AddressOut)
def delete_address(address_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    address = db.query(Address).filter(Address.id == address_id, Address.user_id == user.id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    try:
        db.delete(address)
        db.commit()
        return AddressOut(
            id=address.id,
            street=address.decrypt_address().split(', ')[0],
            city=address.decrypt_address().split(', ')[1],
            state=address.decrypt_address().split(', ')[2],
            postal_code=address.decrypt_address().split(', ')[3]
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete address")

def get_current_user():
    # Placeholder for user authentication
    return User(id=1, username="dummy_user")