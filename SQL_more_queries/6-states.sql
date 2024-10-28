-- create the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)

-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- select a database
USE hbtn_0d_usa;

-- create the table
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256),
    UNIQUE (id),
    PRIMARY KEY (id)
);