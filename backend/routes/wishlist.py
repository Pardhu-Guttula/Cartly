# Epic Title: Implement Shopping Cart and Wishlist Functionality

from flask import Blueprint, request, jsonify
from backend.models.wishlist import Wishlist
from backend.models.wishlist_item import WishlistItem
from backend.models.product import Product
from backend import db

wishlist_bp = Blueprint('wishlist', __name__)

@wishlist_bp.route('/wishlist', methods=['GET'])
def get_wishlist():
    user_id = request.args.get('user_id', type=int)
    wishlist = Wishlist.query.filter_by(user_id=user_id).first()

    if wishlist:
        wishlist_items = [{
            'product_id': item.product_id,
            'product_name': item.product.name,
            'product_price': str(item.product.price)
        } for item in wishlist.wishlist_items]

        return jsonify({
            'user_id': wishlist.user_id,
            'wishlist_items': wishlist_items
        })
    
    return jsonify({'message': 'Wishlist not found'}), 404

@wishlist_bp.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    data = request.get_json()
    user_id = data['user_id']
    product_id = data['product_id']

    wishlist = Wishlist.query.filter_by(user_id=user_id).first()
    if not wishlist:
        wishlist = Wishlist(user_id=user_id)
        db.session.add(wishlist)
        db.session.commit()

    wishlist_item = WishlistItem.query.filter_by(wishlist_id=wishlist.id, product_id=product_id).first()
    if not wishlist_item:
        wishlist_item = WishlistItem(wishlist_id=wishlist.id, product_id=product_id)
        db.session.add(wishlist_item)
        db.session.commit()

    return jsonify({'message': 'Item added to wishlist'})

@wishlist_bp.route('/wishlist/<int:product_id>', methods=['DELETE'])
def remove_from_wishlist(product_id):
    user_id = request.args.get('user_id', type=int)
    wishlist = Wishlist.query.filter_by(user_id=user_id).first()

    if not wishlist:
        return jsonify({'message': 'Wishlist not found'}), 404

    wishlist_item = WishlistItem.query.filter_by(wishlist_id=wishlist.id, product_id=product_id).first()
    if wishlist_item:
        db.session.delete(wishlist_item)
        db.session.commit()
        return jsonify({'message': 'Item removed from wishlist'})

    return jsonify({'message': 'Item not found in wishlist'}), 404