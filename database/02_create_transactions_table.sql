-- Epic Title: Integrate Promotion System with Payment System

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT NOT NULL,
    discount FLOAT DEFAULT 0.0,
    final_amount FLOAT NOT NULL,
    promo_code VARCHAR(20),
    status VARCHAR(20) DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    promotion_id INT,
    FOREIGN KEY (promotion_id) REFERENCES promotions(id)
);