-- Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

CREATE TABLE cart_items (
    id SERIAL PRIMARY KEY,
    cart_id INTEGER NOT NULL REFERENCES carts(id),
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    price_per_unit NUMERIC NOT NULL,
    total_price NUMERIC NOT NULL
);