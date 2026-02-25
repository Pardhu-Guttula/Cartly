-- Epic Title: Develop PostgreSQL Database for Performance Metrics

CREATE TABLE user_behavior (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    action VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

### Dependencies
Below are the dependencies required for the setup: