-- Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

CREATE TABLE wishlists (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE
);