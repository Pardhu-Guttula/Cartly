# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

marketplace_expansion_bp = Blueprint('marketplace_expansion', __name__)

from . import expansion_controller