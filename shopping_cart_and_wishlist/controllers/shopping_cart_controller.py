# Epic Title: Implement shopping cart and wishlist functionality

from flask import Blueprint, request, jsonify
from backend import db
from shopping_cart_and_wishlist.models.shopping_cart import ShoppingCart
from shopping_cart_and_wishlist.models.shopping_cart_item import ShoppingCartItem

shopping_cart_bp = Blueprint('shopping_cart', __name__)

@shopping_cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id: int):
    cart = ShoppingCart.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({"message": "Cart not found"}), 404

    return jsonify({
        "id": cart.id,
        "user_id": cart.user_id,
        "total_price": cart.total_price,
        "items": [
            {
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price": item.price
            } for item in cart.items
        ]
    })

@shopping_cart_bp.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    price = data.get('price')

    cart = ShoppingCart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = ShoppingCart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()

    cart_item = ShoppingCartItem(
        product_id=product_id,
        cart_id=cart.id,
        quantity=quantity,
        price=price
    )

    cart.total_price += quantity * price
    db.session.add(cart_item)
    db.session.commit()

    return jsonify({"message": "Item added to cart"}), 200

@shopping_cart_bp.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')

    cart = ShoppingCart.query.filter_by(user_id=user_id).first()
    if not cart:
        return jsonify({"message": "Cart not found"}), 404

    cart_item = ShoppingCartItem.query.filter_by(product_id=product_id, cart_id=cart.id).first()
    if not cart_item:
        return jsonify({"message": "Item not found in cart"}), 404

    cart.total_price -= cart_item.quantity * cart_item.price
    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({"message": "Item removed from cart"}), 200