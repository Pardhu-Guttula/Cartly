# Epic Title: Develop PostgreSQL Database for Performance Metrics

from backend.admin_dashboard.repositories.metrics_repository import MetricsRepository

class MetricsService:

    @staticmethod
    def store_performance_metric(metric_name: str, metric_value: float) -> None:
        MetricsRepository.store_performance_metric(metric_name, metric_value)

    @staticmethod
    def store_user_behavior(user_id: int, behavior: str) -> None:
        MetricsRepository.store_user_behavior(user_id, behavior)

    @staticmethod
    def query_metrics() -> list:
        return MetricsRepository.query_metrics()