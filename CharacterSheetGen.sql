CREATE DATABASE CharacterSheetGen;

USE CharacterSheetGen;

SHOW databases;

CREATE TABLE account (
	user_name varchar(50) PRIMARY KEY,
	password varchar(10) NOT NULL
	);


CREATE TABLE CharacterDetails (
	id int auto_increment PRIMARY KEY,
	firstname varchar(50) NOT NULL,
	surname varchar(50) NOT NULL,
	age int,
	birthday datetime,
	ZodiacSign varchar(50),
	jobtitle varchar(50),
	Gender varchar(50),
	sexuality varchar(50)
	);

CREATE TABLE Traits (
	character_id int,
	likes varchar(50),
	dislikes varchar(50),
	aspiration varchar(50),
	hobbies varchar(50),
	accent varchar(50)
	);

CREATE TABLE apperence (
	character_id int,
	eye_colour varchar(50),
	hair_colour varchar(50),
	hair_style varchar(50),
	hair_length varchar(50),
	tatoos varchar(50)
	);

CREATE TABLE relationships (
	character1_id int,
	character1_firstname varchar(50),
	character1_surname varchar(50),
	character2_id int,
	character2_firstname varchar(50),
	character2_surname varchar(50),
	relationship varchar(50)
	);

CREATE TABLE tatoos (
	character_id int,
	tatoo_name varchar(50),
	tatoo_size varchar(50),
	tatoo_location varchar(50)
	);

ALTER TABLE CharacterDetails ADD user_name varchar(50) PRIMARY KEY;
ALTER TABLE CharacterDetails DROP password;

