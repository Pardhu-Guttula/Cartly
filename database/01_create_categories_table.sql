-- Epic Title: Ensure Data Integrity and Referential Integrity in Product-Category Models

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL CHECK (char_length(name) > 0),
    description VARCHAR(255),
    parent_id INTEGER REFERENCES categories(id)
);