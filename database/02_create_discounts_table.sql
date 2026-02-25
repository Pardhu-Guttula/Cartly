-- Epic Title: Store Promotion and Discount Data in PostgreSQL

CREATE TABLE discounts (
    id SERIAL PRIMARY KEY,
    discount_amount FLOAT NOT NULL,
    promotion_id INTEGER NOT NULL,
    FOREIGN KEY (promotion_id) REFERENCES promotions (id)
);