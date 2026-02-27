import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient
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


def test_successful_signup(test_client: FlaskClient):
    response = test_client.post('/api/user_authentication/signup', json={
        'email': 'test@example.com',
        'password': 'ValidPassword123'
    })
    data = json.loads(response.data)

    assert response.status_code == 201
    assert data['message'] == 'User account created successfully'


def test_duplicate_email_signup(test_client: FlaskClient):
    # Assuming 'test@example.com' already exists in the database
    response = test_client.post('/api/user_authentication/signup', json={
        'email': 'test@example.com',
        'password': 'ValidPassword123'
    })
    data = json.loads(response.data)

    assert response.status_code == 409
    assert data['message'] == 'Email is already in use'


def test_invalid_password_signup(test_client: FlaskClient):
    response = test_client.post('/api/user_authentication/signup', json={
        'email': 'test@example.com',
        'password': '123'
    })
    data = json.loads(response.data)

    assert response.status_code == 400
    assert data['message'] == 'Password does not meet the complexity requirements'


def test_successful_login(test_client: FlaskClient):
    response = test_client.post('/api/user_authentication/login', json={
        'email': 'test@example.com',
        'password': 'ValidPassword123'
    })
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'access_token' in data


def test_invalid_credentials_login(test_client: FlaskClient):
    response = test_client.post('/api/user_authentication/login', json={
        'email': 'test@example.com',
        'password': 'WrongPassword'
    })
    data = json.loads(response.data)

    assert response.status_code == 401
    assert data['message'] == 'Invalid login credentials'


def test_account_lockout(test_client: FlaskClient):
    # Assuming the account is locked after 3 failed attempts
    for _ in range(3):
        test_client.post('/api/user_authentication/login', json={
            'email': 'test@example.com',
            'password': 'WrongPassword'
        })
    response = test_client.post('/api/user_authentication/login', json={
        'email': 'test@example.com',
        'password': 'ValidPassword123'
    })
    data = json.loads(response.data)

    assert response.status_code == 403
    assert data['message'] == 'Account is locked'
