-- Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

CREATE TABLE carts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total_price NUMERIC NOT NULL DEFAULT 0
);