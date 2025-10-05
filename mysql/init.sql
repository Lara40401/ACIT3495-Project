-- create "users" table: for Authentication
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
);

-- insert initial users
INSERT INTO users (username, password) VALUES ('alice', '1234');
INSERT INTO users (username, password) VALUES ('bob', '1234');

-- create "grades" table: for Enter Data
CREATE TABLE IF NOT EXISTS grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    grades FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
