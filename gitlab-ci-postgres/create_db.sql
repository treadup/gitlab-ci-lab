-- This script creates a database 'places' and a user 'traveler'
-- with password 'ticket'. This database is used for local development.

CREATE DATABASE places;
CREATE USER traveler WITH ENCRYPTED PASSWORD 'ticket';
GRANT ALL PRIVILEGES ON DATABASE places TO traveler;
