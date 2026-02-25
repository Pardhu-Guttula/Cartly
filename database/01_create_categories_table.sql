-- Epic Title: Design PostgreSQL Data Models for Categories

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    parent_id INTEGER REFERENCES categories(id)
);