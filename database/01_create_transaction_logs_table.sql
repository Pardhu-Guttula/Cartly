-- Epic Title: Log and store transactions securely

CREATE TABLE transaction_logs (
    id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(50) NOT NULL,
    order_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    payment_gateway VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);