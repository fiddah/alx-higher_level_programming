-- creates the MySQL server user user_0d_2.
-- user_0d_2 should have only SELECT privilege on your MySQL server
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the user user_0d_2 already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
