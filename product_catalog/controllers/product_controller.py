# Epic Title: Implement product management functionality

from flask import Blueprint, request, jsonify
from backend import db
from product_catalog.models.product import Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')

    new_product = Product(name=name, description=description, price=price)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added successfully"}), 201

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def edit_product(product_id):
    data = request.get_json()
    product = Product.query.get_or_404(product_id)

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)

    db.session.commit()

    return jsonify({"message": "Product updated successfully"}), 200

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def view_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "created_at": product.created_at
    })

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted successfully"}), 200