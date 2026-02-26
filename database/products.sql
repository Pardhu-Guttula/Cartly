# Epic Title: Design PostgreSQL data models for products

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1024) NOT NULL,
    price FLOAT NOT NULL,
    category_id INTEGER NOT NULL,
    inventory INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);