# Epic Title: Develop PostgreSQL Database for Performance Metrics

from backend import db

class MetricsRepository:

    @staticmethod
    def store_performance_metric(metric_name: str, metric_value: float) -> None:
        query = "INSERT INTO performance_metrics (metric_name, metric_value) VALUES (%s, %s)"
        db.execute(query, (metric_name, metric_value))
        db.commit()

    @staticmethod
    def store_user_behavior(user_id: int, behavior: str) -> None:
        query = "INSERT INTO user_behavior (user_id, behavior) VALUES (%s, %s)"
        db.execute(query, (user_id, behavior))
        db.commit()

    @staticmethod
    def query_metrics() -> list:
        query = "SELECT * FROM performance_metrics"
        return db.execute(query).fetchall()