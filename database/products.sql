# Epic Title: Ensure data integrity and referential integrity in product-category models

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1024) NOT NULL,
    price FLOAT NOT NULL CHECK (price >= 0.0),
    category_id INTEGER NOT NULL,
    inventory INTEGER NOT NULL CHECK (inventory >= 0),
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
);