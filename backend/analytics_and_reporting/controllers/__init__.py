# Epic Title: Ensure Modular Architecture for Easy Integration

from flask import Blueprint

analytics_reporting_bp = Blueprint('analytics_reporting', __name__)

from . import analytics_controller