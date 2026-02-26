# Epic Title: Implement Shopping Cart and Wishlist Functionality

from flask import Blueprint, request, jsonify
from backend.models.cart import Cart
from backend.models.cart_item import CartItem
from backend.models.product import Product
from backend import db

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['GET'])
def get_cart():
    user_id = request.args.get('user_id', type=int)
    cart = Cart.query.filter_by(user_id=user_id).first()

    if cart:
        cart_items = [{
            'product_id': item.product_id,
            'quantity': item.quantity,
            'product_name': item.product.name,
            'product_price': str(item.product.price),
            'total_price': str(item.product.price * item.quantity)
        } for item in cart.cart_items]

        return jsonify({
            'user_id': cart.user_id,
            'total_price': str(cart.total_price),
            'cart_items': cart_items
        })
    
    return jsonify({'message': 'Cart not found'}), 404

@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data['user_id']
    product_id = data['product_id']
    quantity = data.get('quantity', 1)

    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    cart.total_price += Product.query.get(product_id).price * quantity
    db.session.commit()

    return jsonify({'message': 'Item added to cart'})

@cart_bp.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    user_id = request.args.get('user_id', type=int)
    cart = Cart.query.filter_by(user_id=user_id).first()

    if not cart:
        return jsonify({'message': 'Cart not found'}), 404

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item:
        cart.total_price -= cart_item.product.price * cart_item.quantity
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'message': 'Item removed from cart'})

    return jsonify({'message': 'Item not found in cart'}), 404