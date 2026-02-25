-- Epic Title: Integrate Promotion System with Order Management

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    total_amount FLOAT NOT NULL,
    discount_amount FLOAT DEFAULT 0.0,
    final_amount FLOAT NOT NULL,
    promotion_code VARCHAR(20),
    status VARCHAR(20) DEFAULT 'pending',
    promotion_id INTEGER,
    FOREIGN KEY (promotion_id) REFERENCES promotions(id)
);

### Dependencies
Below are the dependencies required for the setup: