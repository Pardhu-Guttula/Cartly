-- Epic Title: Design PostgreSQL Data Models for Products

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);