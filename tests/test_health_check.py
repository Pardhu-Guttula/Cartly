# File: tests/test_health_check.py

import unittest
from flask import Flask
from your_module_path import product_catalog_bp

class TestHealthCheck(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(product_catalog_bp)
        self.client = self.app.test_client()

    def test_health_check_success(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'Product Catalog API is healthy'})

    def test_health_check_invalid_method(self):
        # Testing invalid method (POST) should return 405 Method Not Allowed
        response = self.client.post('/health')
        self.assertEqual(response.status_code, 405)

    def test_health_check_invalid_route(self):
        # Testing invalid route should return 404 Not Found
        response = self.client.get('/invalid_route')
        self.assertEqual(response.status_code, 404)
