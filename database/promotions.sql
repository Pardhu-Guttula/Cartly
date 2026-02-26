# Epic Title: Apply Promotions During Checkout

CREATE TABLE IF NOT EXISTS promotions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_amount INT NOT NULL,
    expiry_date DATETIME NOT NULL,
    active BOOLEAN DEFAULT TRUE
);