from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.models import Cart, CartItem
from backend.schemas import Cart as CartSchema, CartItem as CartItemSchema, CartUpdate
from backend.services.database import get_db

# Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

router = APIRouter()

@router.post("/add_item", response_model=CartSchema)
def add_item_to_cart(cart_item: CartItemSchema, db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.user_id == cart_item.user_id).first()

    if not cart:
        cart = Cart(user_id=cart_item.user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    
    item = db.query(CartItem).filter(CartItem.cart_id == cart.id,
                                     CartItem.product_id == cart_item.product_id).first()
    
    if item:
        item.quantity += cart_item.quantity
        item.total_price = item.quantity * item.price_per_unit
    else:
        item = CartItem(
            cart_id=cart.id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            price_per_unit=cart_item.price_per_unit,
            total_price=cart_item.quantity * cart_item.price_per_unit
        )
        db.add(item)
    
    db.commit()
    db.refresh(cart)
    
    cart.total_price = sum(item.total_price for item in cart.items)
    db.commit()
    return cart

@router.post("/remove_item", response_model=CartSchema)
def remove_item_from_cart(cart_update: CartUpdate, db: Session = Depends(get_db)):
    cart = db.query(Cart).filter(Cart.user_id == cart_update.user_id).first()

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    item = db.query(CartItem).filter(CartItem.cart_id == cart.id,
                                     CartItem.product_id == cart_update.product_id).first()
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in cart")

    if cart_update.quantity >= item.quantity:
        db.delete(item)
    else:
        item.quantity -= cart_update.quantity
        item.total_price = item.quantity * item.price_per_unit
        db.add(item)
    
    db.commit()

    cart.total_price = sum(item.total_price for item in cart.items)
    db.commit()
    return cart