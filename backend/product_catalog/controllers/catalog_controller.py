# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import jsonify
from . import product_catalog_bp

@product_catalog_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'Product Catalog API is healthy'})