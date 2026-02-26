# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

checkout_process_bp = Blueprint('checkout_process', __name__)

from . import checkout_controller