-- Epic Title: Develop Frontend Interface for Promotions

CREATE TABLE promotions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    discount_amount FLOAT NOT NULL,
    expiration_date DATE NOT NULL
);