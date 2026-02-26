# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

user_accounts_bp = Blueprint('user_accounts', __name__)

from . import accounts_controller