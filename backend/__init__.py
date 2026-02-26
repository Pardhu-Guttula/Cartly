# Epic Title: Apply Promotions During Checkout

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/checkoutdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from checkout_process.controllers.checkout_controller import checkout_bp
        app.register_blueprint(checkout_bp, url_prefix='/api')

    return app