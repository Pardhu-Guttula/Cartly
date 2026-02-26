# Epic Title: User Signup Functionality

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL UNIQUE,
    credentials_id INT NOT NULL,
    FOREIGN KEY (credentials_id) REFERENCES credentials(id)
);