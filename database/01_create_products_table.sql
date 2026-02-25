-- Epic Title: Implement product management functionality

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price NUMERIC NOT NULL,
    inventory INTEGER NOT NULL
);