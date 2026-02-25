-- Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price NUMERIC NOT NULL CHECK (price > 0),
    category_id INTEGER NOT NULL REFERENCES categories(id),
    inventory INTEGER NOT NULL CHECK (inventory >= 0)
);