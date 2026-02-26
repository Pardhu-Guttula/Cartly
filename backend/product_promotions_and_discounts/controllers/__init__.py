# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

promotions_discounts_bp = Blueprint('promotions_discounts', __name__)

from . import promotions_controller