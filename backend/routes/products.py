# Epic Title: Develop Reusable Product Browsing Components

from flask import Blueprint, request, jsonify
from backend.models.product import Product
from backend import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    products_pagination = Product.query.paginate(page, per_page, False)

    products_list = [{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': str(product.price),
        'inventory': product.inventory,
        'rating': str(product.rating)
    } for product in products_pagination.items]

    return jsonify({
        'products': products_list,
        'total': products_pagination.total,
        'pages': products_pagination.pages,
        'current_page': products_pagination.page
    })