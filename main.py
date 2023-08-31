CREATE DATABASE company;
USE company;

CREATE TABLE companies (
 	name varchar(50),
 	age integer,
 	company_email varchar(50)
);

-- INSERT INTO companies (name, age, company_email)
-- VALUES
-- ('SV Motors', 15, 'sv@mail.ru'),
-- ('ATR', 20, 'atr@mail.ru'),
-- ('Doctor Motors', 14, 'dm@tut.by');

INSERT INTO companies (name, age, company_email)
VALUES
('Michlen', 30, 'mch@mail.ru'),
('Mannol', 23, 'man@mail.ru'),
('Shell', 27, 'shell@qmail.ru');

USE company;
SELECT * FROM companies;

USE company;
CREATE TABLE users (
 	first_name varchar(20),
 	date_start varchar(10),
 	manager_name varchar(20)
);

-- INSERT INTO users (first_name, date_start, manager_name)
-- VALUES
-- ('Alex', '25.10.2023', 'Moscow'),
-- ('Tom', '26.10.2023', 'Minsk'),
-- ('Nick', '27.10.2023', 'Vitebsk');

INSERT INTO users (first_name, date_start, manager_name)
VALUES
('Vlad', '15.11.2023', 'Moscow'),
('Dima', '16.11.2023', 'Minsk'),
('Nikita', '17.11.2023', 'Vitebsk');

USE company;
SELECT * FROM users;
























import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1005Lavr__'
    )

curs = mydb.cursor()

# curs.execute('CREATE DATEBASE newbaseone')

sqlQuery = "insert into users11 (first_name varchar(25), date_start varchar(10), manager_name varchar(20) values (%s, %s, %s)"
sqlValues = [
	('Alex', '25.10.2023', 'Moscow'),
    ('Tom', '26.10.2023', 'Minsk'),
    ('Nick', '27.10.2023', 'Vitebsk'),
]

curs.executemany(sqlQuery, sqlValues)

