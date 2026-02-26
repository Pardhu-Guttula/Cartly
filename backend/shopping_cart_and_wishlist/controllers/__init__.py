# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

shopping_cart_wishlist_bp = Blueprint('shopping_cart_wishlist', __name__)

from . import cart_wishlist_controller