from flask import Flask
from backend.routes.user_route import user_bp
import logging

# Epic Title: User Signup Functionality

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app