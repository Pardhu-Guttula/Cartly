-- Epic Title: Implement Shopping Cart and Wishlist Functionality

CREATE TABLE carts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total_price NUMERIC NOT NULL DEFAULT 0
);