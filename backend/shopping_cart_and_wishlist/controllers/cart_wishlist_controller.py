# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import shopping_cart_wishlist_bp

@shopping_cart_wishlist_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Shopping Cart and Wishlist API is healthy'})