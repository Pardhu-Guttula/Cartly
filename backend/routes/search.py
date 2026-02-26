# Epic Title: Implement Efficient Product Search Functionality

from flask import Blueprint, request, jsonify
from backend.models.product import Product
from backend import db

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    category = request.args.get('category', None)
    min_price = request.args.get('min_price', None)
    max_price = request.args.get('max_price', None)
    availability = request.args.get('availability', None)
    sort_by = request.args.get('sort_by', 'relevance')

    filters = [Product.name.like(f'%{query}%') | Product.description.like(f'%{query}%')]

    if category:
        filters.append(Product.category_id == category)
    if min_price:
        filters.append(Product.price >= float(min_price))
    if max_price:
        filters.append(Product.price <= float(max_price))
    if availability is not None:
        filters.append(Product.inventory > 0 if availability == 'in_stock' else Product.inventory == 0)
    
    products_query = db.session.query(Product).filter(*filters)

    if sort_by == 'price':
        products_query = products_query.order_by(Product.price)
    elif sort_by == 'rating':
        products_query = products_query.order_by(Product.rating.desc())
    else:
        products_query = products_query.order_by(Product.name)

    products = products_query.all()
    products_list = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': str(product.price), 'inventory': product.inventory, 'rating': str(product.rating)} for product in products]

    return jsonify(products_list)