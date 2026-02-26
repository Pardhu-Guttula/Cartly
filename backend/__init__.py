# Epic Title: Integrate Promotion System with Payment System

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/checkoutdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from product_promotions_and_discounts.controllers.promotion_controller import promotion_bp
        from checkout_process.controllers.payment_controller import payment_bp

        app.register_blueprint(promotion_bp, url_prefix='/api')
        app.register_blueprint(payment_bp, url_prefix='/api')

    return app