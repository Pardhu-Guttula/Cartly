import pytest
from flask import Flask
from backend.checkout_process.controllers import checkout_process_bp

@pytest.fixture(scope='module')
def test_client():
    app = Flask(__name__)
    app.register_blueprint(checkout_process_bp, url_prefix='/api/checkout_process')
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


def test_health_check(test_client):
    response = test_client.get('/api/checkout_process/health')
    assert response.status_code == 200
    assert response.json == {'status': 'Checkout Process API is healthy'}
