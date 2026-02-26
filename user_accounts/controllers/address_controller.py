# Epic Title: Address Data Security

from flask import Blueprint, request, jsonify
from backend import db
from user_accounts.models.address import Address
from functools import wraps

address_bp = Blueprint('address', __name__)

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get("Authorization") == "Bearer your-secure-token":
            return jsonify({"error": "Unauthorized access"}), 403
        return f(*args, **kwargs)
    return decorated_function

@address_bp.route('/address', methods=['POST'])
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

    address = Address(user_id=user_id, street=street, city=city, state=state, postal_code=postal_code, country=country)
    db.session.add(address)
    db.session.commit()
    return jsonify({"message": "Address saved successfully"}), 201

@address_bp.route('/address', methods=['GET'])
@authorize
def get_addresses():
    user_id = request.args.get('user_id')

    addresses = Address.query.filter_by(user_id=user_id).all()
    if not addresses:
        return jsonify({"message": "No saved addresses found"}), 200

    address_list = [{
        "id": address.id,
        "street": Address.decrypt_data(address.street),
        "city": Address.decrypt_data(address.city),
        "state": Address.decrypt_data(address.state),
        "postal_code": Address.decrypt_data(address.postal_code),
        "country": Address.decrypt_data(address.country)
    } for address in addresses]

    return jsonify(address_list), 200