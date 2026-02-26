# File: tests/test_catalog_controller.py

import unittest
from flask import Flask
from flask.testing import FlaskClient
from mypackage.catalog_controller import catalog_controller

class TestCatalogController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = Flask(__name__)
        app.register_blueprint(catalog_controller)
        cls.client: FlaskClient = app.test_client()

    def test_get_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_get_product_by_id_existing(self):
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)

    def test_get_product_by_id_non_existing(self):
        response = self.client.get('/products/999')
        self.assertEqual(response.status_code, 404)

    def test_create_product_success(self):
        response = self.client.post('/products', json={
            'id': 1,
            'name': 'Test Product',
            'price': 100
        })
        self.assertEqual(response.status_code, 201)

    def test_create_product_missing_field(self):
        response = self.client.post('/products', json={
            'name': 'Test Product'
        })
        self.assertEqual(response.status_code, 400)

    def test_update_product_success(self):
        response = self.client.put('/products/1', json={
            'name': 'Updated Product',
            'price': 150
        })
        self.assertEqual(response.status_code, 200)

    def test_update_product_non_existing(self):
        response = self.client.put('/products/999', json={
            'name': 'Updated Product',
            'price': 150
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_product_success(self):
        response = self.client.delete('/products/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_product_non_existing(self):
        response = self.client.delete('/products/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
