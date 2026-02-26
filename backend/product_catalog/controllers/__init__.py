# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

product_catalog_bp = Blueprint('product_catalog', __name__)

from . import catalog_controller