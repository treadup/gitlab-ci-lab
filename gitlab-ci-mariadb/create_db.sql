-- This script creates a database 'places' and a user 'traveler'
-- with password 'ticket'. This database is used for local development.

CREATE DATABASE places;
CREATE USER 'traveler'@'localhost' IDENTIFIED BY 'ticket';
GRANT ALL PRIVILEGES ON 'places' . * TO 'traveler'@'localhost';
FLUSH PRIVILEGES;
