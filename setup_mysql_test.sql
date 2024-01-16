-- Prepares a MySQL server for the project

-- Create a database named 'hbnb_test_db'
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates new user 'hbnb_test'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the database 'hbnb_test_db' to 'hbnb_test'
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- hbnb_dev should have SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
