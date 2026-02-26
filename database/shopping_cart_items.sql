# Epic Title: Implement shopping cart and wishlist functionality

CREATE TABLE IF NOT EXISTS shopping_cart_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    cart_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    price FLOAT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (cart_id) REFERENCES shopping_carts(id) ON DELETE CASCADE
);