# Epic Title: Store Promotion and Discount Data in PostgreSQL

from flask import Blueprint, request, jsonify
from product_promotions_and_discounts.services.promotion_service import PromotionService
from datetime import datetime

promotion_bp = Blueprint('promotion', __name__)

@promotion_bp.route('/promotion', methods=['POST'])
def add_promotion():
    data = request.get_json()
    code = data.get('code')
    discount_amount = data.get('discount_amount')
    expiry_date = datetime.strptime(data.get('expiry_date'), '%Y-%m-%dT%H:%M:%S')
    
    PromotionService.create_promotion(code, discount_amount, expiry_date)
    return jsonify({"message": "Promotion added successfully"}), 201

@promotion_bp.route('/promotion/<string:code>', methods=['PUT'])
def update_promotion(code):
    data = request.get_json()
    discount_amount = data.get('discount_amount')
    expiry_date = datetime.strptime(data.get('expiry_date'), '%Y-%m-%dT%H:%M:%S')
    active = data.get('active')
    
    PromotionService.update_promotion(code, discount_amount, expiry_date, active)
    return jsonify({"message": "Promotion updated successfully"}), 200

@promotion_bp.route('/promotion/<string:code>', methods=['GET'])
def get_promotion(code):
    promotion = PromotionService.get_promotion(code)
    if not promotion:
        return jsonify({"error": "Promotion not found"}), 404
    
    return jsonify({
        "code": promotion.code,
        "discount_amount": promotion.discount_amount,
        "expiry_date": promotion.expiry_date,
        "active": promotion.active
    }), 200

@promotion_bp.route('/promotions', methods=['GET'])
def list_promotions():
    promotions = PromotionService.list_promotions()
    
    return jsonify([{
        "code": promotion.code,
        "discount_amount": promotion.discount_amount,
        "expiry_date": promotion.expiry_date,
        "active": promotion.active
    } for promotion in promotions]), 200