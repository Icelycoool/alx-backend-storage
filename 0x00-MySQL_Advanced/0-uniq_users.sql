-- Creates 'users' table with the following attributes:
-- id (int), email(string), name(string)
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    email VARCHAR(225) UNIQUE NOT NULL,
    name VARCHAR(225)
);