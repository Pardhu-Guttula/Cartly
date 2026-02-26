# Epic Title: Implement shopping cart and wishlist functionality

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/shoppingdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from shopping_cart_and_wishlist.controllers.shopping_cart_controller import shopping_cart_bp
        app.register_blueprint(shopping_cart_bp, url_prefix='/api')

    return app