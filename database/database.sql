CREATE DATABASE IF NOT EXISTS maysan;
use maysan;

CREATE TABLE IF NOT EXISTS user(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS message(
    id INT NOT NULL AUTO_INCREMENT,
    from_ INT NOT NULL,
    to_ INT NOT NULL,
    object_message VARCHAR(100),
    content VARCHAR(8000),
    date_time DATETIME NOT NULL,
    seen BOOLEAN,
    PRIMARY KEY (id),
    FOREIGN KEY (from_) REFERENCES user(id),
    FOREIGN KEY (to_) REFERENCES user(id)
);