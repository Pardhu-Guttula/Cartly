# Epic Title: User Password Security

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from backend.routes.signup import signup_bp
    from backend.routes.login import login_bp
    app.register_blueprint(signup_bp)
    app.register_blueprint(login_bp)

    return app