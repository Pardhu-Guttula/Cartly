# Epic Title: User Password Security

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from user_authentication.controllers.security_controller import security_bp
    app.register_blueprint(security_bp, url_prefix='/api')

    return app