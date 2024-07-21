CREATE DATABASE gymalyticsdb;
CREATE USER 'ldepla'@'localhost' IDENTIFIED BY 'dbpassword';
GRANT ALL PRIVILEGES ON gymalyticsdb.* TO 'ldepla'@'localhost';
FLUSH PRIVILEGES;

