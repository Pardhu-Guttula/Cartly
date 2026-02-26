# Epic Title: Design PostgreSQL Data Models for Categories

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1000),
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);