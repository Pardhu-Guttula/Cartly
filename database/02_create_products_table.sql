-- Epic Title: Design PostgreSQL Data Models for Products

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price NUMERIC NOT NULL,
    category_id INTEGER NOT NULL REFERENCES categories(id),
    inventory INTEGER NOT NULL
);