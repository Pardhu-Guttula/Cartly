-- Epic Title: User Login Functionality

CREATE TABLE sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    jwt_token VARCHAR(255) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);