-- Epic Title: Persist Data with PostgreSQL for Shopping Cart and Wishlist

CREATE TABLE wishlist_items (
    id SERIAL PRIMARY KEY,
    wishlist_id INTEGER NOT NULL REFERENCES wishlists(id),
    product_id INTEGER NOT NULL
);