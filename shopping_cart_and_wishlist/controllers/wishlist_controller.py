# Epic Title: Implement shopping cart and wishlist functionality

from flask import Blueprint, request, jsonify
from backend import db
from shopping_cart_and_wishlist.models.wishlist import Wishlist
from shopping_cart_and_wishlist.models.wishlist_item import WishlistItem

wishlist_bp = Blueprint('wishlist', __name__)

@wishlist_bp.route('/wishlist/<int:user_id>', methods=['GET'])
def get_wishlist(user_id: int):
    wishlist = Wishlist.query.filter_by(user_id=user_id).first()
    if not wishlist:
        return jsonify({"message": "Wishlist not found"}), 404

    return jsonify({
        "id": wishlist.id,
        "user_id": wishlist.user_id,
        "items": [
            {
                "product_id": item.product_id,
            } for item in wishlist.items
        ]
    })

@wishlist_bp.route('/wishlist/add', methods=['POST'])
def add_to_wishlist():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')

    wishlist = Wishlist.query.filter_by(user_id=user_id).first()
    if not wishlist:
        wishlist = Wishlist(user_id=user_id)
        db.session.add(wishlist)
        db.session.commit()

    wishlist_item = WishlistItem(
        product_id=product_id,
        wishlist_id=wishlist.id
    )

    db.session.add(wishlist_item)
    db.session.commit()

    return jsonify({"message": "Item added to wishlist"}), 200

@wishlist_bp.route('/wishlist/remove', methods=['POST'])
def remove_from_wishlist():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')

    wishlist = Wishlist.query.filter_by(user_id=user_id).first()
    if not wishlist:
        return jsonify({"message": "Wishlist not found"}), 404

    wishlist_item = WishlistItem.query.filter_by(product_id=product_id, wishlist_id=wishlist.id).first()
    if not wishlist_item:
        return jsonify({"message": "Item not found in wishlist"}), 404

    db.session.delete(wishlist_item)
    db.session.commit()

    return jsonify({"message": "Item removed from wishlist"}), 200