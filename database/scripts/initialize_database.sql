# Epic Title: Develop Data Processing Backend with Node.js

CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    key VARCHAR(50) NOT NULL,
    value TEXT NOT NULL
);