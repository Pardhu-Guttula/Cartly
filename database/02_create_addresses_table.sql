-- Epic Title: Save User Address

CREATE TABLE addresses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    encrypted_address TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);