-- Epic Title: Implement Shopping Cart and Wishlist Functionality

CREATE TABLE wishlists (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE
);