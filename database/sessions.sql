# Epic Title: User Password Security

CREATE TABLE IF NOT EXISTS sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    jwt_token VARCHAR(512) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);