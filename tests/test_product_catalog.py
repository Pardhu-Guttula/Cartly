# File: tests/test_product_catalog.py

import unittest
from unittest.mock import patch
from myapp import create_app

class ProductCatalogTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'Product Catalog API is healthy'})

    @patch('myapp.product_catalog_bp.jsonify')
    def test_health_check_jsonify_exception(self, mock_jsonify):
        mock_jsonify.side_effect = Exception('jsonify error')
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()