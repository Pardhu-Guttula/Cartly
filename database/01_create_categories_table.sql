-- Epic Title: Implement Efficient Product Search Functionality

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL CHECK (char_length(name) > 0),
    description VARCHAR(255),
    parent_id INTEGER REFERENCES categories(id)
);