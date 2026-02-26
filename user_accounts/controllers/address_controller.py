# Epic Title: Retrieve User Addresses

from flask import Blueprint, request, jsonify
from backend import db
from user_accounts.models.address import Address

address_bp = Blueprint('address', __name__)

@address_bp.route('/address', methods=['GET'])
def get_addresses():
    user_id = request.args.get('user_id')

    addresses = Address.query.filter_by(user_id=user_id).all()
    if not addresses:
        return jsonify({"message": "No saved addresses found"}), 200

    address_list = [{
        "id": address.id,
        "street": address.street,
        "city": address.city,
        "state": address.state,
        "postal_code": address.postal_code,
        "country": address.country
    } for address in addresses]

    return jsonify(address_list), 200