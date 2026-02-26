# Epic Title: Edit User Address

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from backend import db
from user_accounts.models.address import Address
import hashlib

address_bp = Blueprint('address', __name__)

@address_bp.route('/address/<int:address_id>', methods=['PUT'])
def update_address(address_id: int):
    data = request.get_json()
    user_id = data.get('user_id')
    street = data.get('street')
    city = data.get('city')
    state = data.get('state')
    postal_code = data.get('postal_code')
    country = data.get('country')

    if not all([street, city, state, postal_code, country]):
        return jsonify({"error": "All address fields are mandatory"}), 400

    encrypted_postal_code = hashlib.sha256(postal_code.encode()).hexdigest()

    address = Address.query.filter_by(id=address_id, user_id=user_id).first()
    if not address:
        return jsonify({"error": "Address not found"}), 404

    try:
        address.street = street
        address.city = city
        address.state = state
        address.postal_code = encrypted_postal_code
        address.country = country

        db.session.commit()
        return jsonify({"message": "Address updated successfully"}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to update address"}), 500