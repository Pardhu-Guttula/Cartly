-- Epic Title: Store Promotion and Discount Data in PostgreSQL

CREATE TABLE promotions (
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    discount_amount FLOAT NOT NULL,
    expiration_date DATE NOT NULL
);