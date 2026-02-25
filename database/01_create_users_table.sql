-- Epic Title: Address Data Security

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    is_authorized BOOLEAN DEFAULT FALSE
);