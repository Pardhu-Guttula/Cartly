# Epic Title: Save User Address

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from backend import db
from user_accounts.models.user import User
from user_accounts.models.address import Address
import hashlib

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/address', methods=['POST'])
def save_address():
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

    try:
        address = Address(user_id=user_id, street=street, city=city, state=state, postal_code=encrypted_postal_code, country=country)
        db.session.add(address)
        db.session.commit()
        return jsonify({"message": "Address saved successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to save address"}), 500