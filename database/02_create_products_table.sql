-- Epic Title: Implement Shopping Cart and Wishlist Functionality

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price NUMERIC NOT NULL CHECK (price > 0),
    category_id INTEGER NOT NULL REFERENCES categories(id),
    inventory INTEGER NOT NULL CHECK (inventory >= 0)
);