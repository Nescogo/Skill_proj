CREATE DATABASE IF NOT EXISTS boardg;
DROP USER IF EXISTS 'user'@'%';
CREATE USER IF NOT EXISTS 'user'@'%' IDENTIFIED BY 'password';
GRANT SELECT, UPDATE, INSERT ON boardg.* TO 'user'@'%';
FLUSH PRIVILEGES;
USE boardg;
CREATE TABLE IF NOT EXISTS bg(
	game VARCHAR(100) NOT NULL,
	g_type VARCHAR(100) NOT NULL,
	year INT(10) NOT NULL);
INSERT INTO bg(game, g_type, year)
VALUES
	('Brass: Birmingam', 'Euro', '2018'),
	('Pandemic Legacy: Season 1', 'Legacy', '2015'),
	('Twilight Imperium Fourth Edition', '4x Strategy', '2017');
