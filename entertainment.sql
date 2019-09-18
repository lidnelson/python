CREATE DATABASE entertainment;

USE entertainment;

SHOW databases;

CREATE TABLE television (
	ID int auto_increment PRIMARY KEY,
	name varchar(50) NOT NULL, 
	length int, 
	genre varchar(50), 
	rating varchar(10) NOT NULL
	);

DESCRIBE television;

INSERT INTO television VALUES (1,"Star Trek", 128, "scinece fiction", "PG");
