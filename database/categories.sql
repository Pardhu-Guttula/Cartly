# Epic Title: Ensure Data Integrity and Referential Integrity in Product-Category Models

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1000),
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);