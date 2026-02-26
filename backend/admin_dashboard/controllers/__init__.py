# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

admin_dashboard_bp = Blueprint('admin_dashboard', __name__)

from . import admin_controller