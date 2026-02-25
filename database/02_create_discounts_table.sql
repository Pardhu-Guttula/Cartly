-- Epic Title: Develop Frontend Interface for Promotions

CREATE TABLE discounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    discount_amount FLOAT NOT NULL,
    promotion_id INT NOT NULL,
    FOREIGN KEY (promotion_id) REFERENCES promotions(id)
);