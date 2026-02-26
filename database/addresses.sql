# Epic Title: Address Data Security

CREATE TABLE IF NOT EXISTS addresses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    postal_code VARCHAR(64) NOT NULL, 
    country VARCHAR(100) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);