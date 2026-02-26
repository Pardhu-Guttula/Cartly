# Epic Title: Develop Visualization Front-end with Next.js

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/analyticsdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from analytics_and_reporting.controllers.data_controller import data_bp
        app.register_blueprint(data_bp, url_prefix='/api')

    return app