from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models import Wishlist, WishlistItem
from backend.schemas import Wishlist as WishlistSchema, WishlistItem as WishlistItemSchema
from backend.services.database import get_db

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

router = APIRouter()

@router.post("/add_item", response_model=WishlistSchema)
def add_item_to_wishlist(wishlist_item: WishlistItemSchema, db: Session = Depends(get_db)):
    wishlist = db.query(Wishlist).filter(Wishlist.user_id == wishlist_item.user_id).first()

    if not wishlist:
        wishlist = Wishlist(user_id=wishlist_item.user_id)
        db.add(wishlist)
        db.commit()
        db.refresh(wishlist)
    
    item = db.query(WishlistItem).filter(WishlistItem.wishlist_id == wishlist.id,
                                         WishlistItem.product_id == wishlist_item.product_id).first()
    
    if item:
        raise HTTPException(status_code=400, detail="Item already in wishlist")
    
    item = WishlistItem(
        wishlist_id=wishlist.id,
        product_id=wishlist_item.product_id,
    )
    db.add(item)
    db.commit()
    db.refresh(wishlist)
    
    return wishlist

@router.post("/remove_item", response_model=WishlistSchema)
def remove_item_from_wishlist(wishlist_item: WishlistItemSchema, db: Session = Depends(get_db)):
    wishlist = db.query(Wishlist).filter(Wishlist.user_id == wishlist_item.user_id).first()

    if not wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")

    item = db.query(WishlistItem).filter(WishlistItem.wishlist_id == wishlist.id,
                                         WishlistItem.product_id == wishlist_item.product_id).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in wishlist")

    db.delete(item)
    db.commit()
    db.refresh(wishlist)
    
    return wishlist