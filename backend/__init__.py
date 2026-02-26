# Epic Title: Store Promotion and Discount Data in PostgreSQL

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/promotionsdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from product_promotions_and_discounts.controllers.promotion_controller import promotion_bp
        app.register_blueprint(promotion_bp, url_prefix='/api')

    return app