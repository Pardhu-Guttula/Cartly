import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient
from backend.user_authentication.controllers.authentication_controller import health_check
import json

db = SQLAlchemy()

@pytest.fixture(scope='module')
def test_client():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user:password@localhost/dbname'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(flask_app)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    testing_client = flask_app.test_client()

    # Establish an application context before running tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


def test_health_check(test_client: FlaskClient):
    response = test_client.get('/api/user_authentication/health')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['status'] == 'User Authentication API is healthy'