# Epic Title: Design PostgreSQL Data Models for Categories

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1000),
    price NUMERIC(10, 2) NOT NULL,
    category_id INTEGER NOT NULL,
    inventory INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);