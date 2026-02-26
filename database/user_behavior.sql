# Epic Title: Develop PostgreSQL Database for Performance Metrics

CREATE TABLE IF NOT EXISTS user_behavior (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    behavior VARCHAR(255) NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);