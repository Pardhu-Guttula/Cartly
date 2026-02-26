# Epic Title: Implement Shopping Cart and Wishlist Functionality

CREATE TABLE IF NOT EXISTS wishlists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL
);