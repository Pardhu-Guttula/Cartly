# Epic Title: Store Promotion and Discount Data in PostgreSQL

CREATE TABLE IF NOT EXISTS promotions (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_amount INT NOT NULL,
    expiry_date TIMESTAMPTZ NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT Now(),
    updated_at TIMESTAMPTZ DEFAULT Now()
);

CREATE INDEX idx_promotions_code ON promotions(code);
CREATE INDEX idx_promotions_expiry_date ON promotions(expiry_date);