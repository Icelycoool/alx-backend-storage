-- Creates a 'users' table with the followng atrributes
-- id(integer), email(string), name(string), country(enumeration)
CREATE TABLE IF NOT EXISTS users (
    `id` INT AUTO_INCREMENT NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
    PRIMARY KEY(`id`)
);