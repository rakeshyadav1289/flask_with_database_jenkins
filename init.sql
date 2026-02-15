CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('user','admin') DEFAULT 'user'
);

-- Insert admin user with bcrypt hash for "admin123"
INSERT INTO users (username, password, role)
VALUES ('admin', '$2b$12$KIXQ6nXWZpQ4Y5YwXQnY9uYwFZk9vZpYk9uZkYwFZk9vZpYk9u', 'admin');

CREATE USER 'flaskuser'@'%' IDENTIFIED BY 'flaskpass';
GRANT ALL PRIVILEGES ON flask_users.* TO 'flaskuser'@'%';
FLUSH PRIVILEGES;

