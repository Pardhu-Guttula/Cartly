# Epic Title: Develop PostgreSQL Database for Performance Metrics

from flask import Blueprint, request, jsonify
from backend.admin_dashboard.services.metrics_service import MetricsService

metrics_bp = Blueprint('metrics', __name__)

@metrics_bp.route('/metrics/performance', methods=['POST'])
def store_performance_metric():
    data = request.get_json()
    metric_name = data['metric_name']
    metric_value = data['metric_value']
    MetricsService.store_performance_metric(metric_name, metric_value)
    return jsonify({"message": "Performance metric stored successfully"}), 201

@metrics_bp.route('/metrics/user_behavior', methods=['POST'])
def store_user_behavior():
    data = request.get_json()
    user_id = data['user_id']
    behavior = data['behavior']
    MetricsService.store_user_behavior(user_id, behavior)
    return jsonify({"message": "User behavior stored successfully"}), 201

@metrics_bp.route('/metrics', methods=['GET'])
def query_metrics():
    metrics = MetricsService.query_metrics()
    return jsonify(metrics), 200