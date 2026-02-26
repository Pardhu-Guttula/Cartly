# Epic Title: Integrate Promotion System with Payment System

CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    promotion_code VARCHAR(50) NULL
);