# Epic Title: Develop Visualization Front-end with Next.js

from flask import Blueprint, jsonify
import random

data_bp = Blueprint('data', __name__)

@data_bp.route('/data', methods=['GET'])
def get_data():
    # Simulate fetching data from a database
    data = [
        {"label": f"Item {i}", "value": random.randint(1, 100)}
        for i in range(1, 11)
    ]
    return jsonify(data)