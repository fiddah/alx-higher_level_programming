-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
CREATE TABLE IF NOT EXIST hbtn_0d_usa.states(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
