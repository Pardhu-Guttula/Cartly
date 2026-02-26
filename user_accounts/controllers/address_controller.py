# Epic Title: Delete User Address

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from backend import db
from user_accounts.models.address import Address

address_bp = Blueprint('address', __name__)

@address_bp.route('/address/<int:address_id>', methods=['DELETE'])
def delete_address(address_id: int):
    data = request.get_json()
    user_id = data.get('user_id')

    address = Address.query.filter_by(id=address_id, user_id=user_id).first()
    if not address:
        return jsonify({"error": "Address not found"}), 404

    try:
        db.session.delete(address)
        db.session.commit()
        return jsonify({"message": "Address deleted successfully"}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to delete address"}), 500