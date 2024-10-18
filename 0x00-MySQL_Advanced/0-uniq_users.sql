-- Creates 'users' table with the following attributes:
-- id (int), email(string), name(string)
CREATE TABLE IF NOT EXISTS users (
    `id` INT AUTO_INCREMENT NOT NULL,
    `email` VARCHAR(225) UNIQUE NOT NULL,
    `name` VARCHAR(225),
    PRIMARY KEY (`id`)
);