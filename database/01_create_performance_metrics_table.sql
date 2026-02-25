-- Epic Title: Develop PostgreSQL Database for Performance Metrics

CREATE TABLE performance_metrics (
    id SERIAL PRIMARY KEY,
    metric_name VARCHAR(255) NOT NULL,
    value FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL
);