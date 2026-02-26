# Epic Title: Save User Address

from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.models.address import Address
from backend import db

address_bp = Blueprint('address', __name__)

@address_bp.route('/address', methods=['POST'])
def save_address():
    data = request.get_json()
    user_id = data.get('user_id')
    address_line1 = data.get('address_line1')
    city = data.get('city')
    state = data.get('state')
    postal_code = data.get('postal_code')

    if not (user_id and address_line1 and city and state and postal_code):
        return jsonify({'message': 'Missing mandatory fields'}), 400
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if not postal_code.isdigit():
        return jsonify({'message': 'Invalid postal code'}), 400

    new_address = Address(user_id=user_id, address_line1=address_line1, address_line2=data.get('address_line2'), city=city, state=state, postal_code=postal_code)
    db.session.add(new_address)
    db.session.commit()
    
    return jsonify({'message': 'Address saved successfully'})