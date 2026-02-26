# Epic Title: Develop PostgreSQL Database for Performance Metrics

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/analyticsdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from admin_dashboard.controllers.metrics_controller import metrics_bp
        app.register_blueprint(metrics_bp, url_prefix='/api')

    return app