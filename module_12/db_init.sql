/*
    Title: whatabook db_init.sql
    Author: John Wall
    Date: 11 August 2022
    Description: WhatABook initilization script
*/


/*
    Create the whatabook database
*/
CREATE DATABASE whatabook;

/*
    Create the whatabook user and grant all privileges to them on the localhost
*/
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

/*
    Test if the four tables exist already and drop if they do
*/
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create the four tables to be used: Store, Table, Book, User. Establish the appropriate
    Primary and Foregin keys.
*/
CREATE TABLE store( 
    store_id INT NOT NULL AUTO_INCREMENT, 
    locale VARCHAR(500) NOT NULL, 
    PRIMARY KEY(store_id) 
);
CREATE TABLE book( 
    book_id INT NOT NULL AUTO_INCREMENT, 
    book_name VARCHAR(200) NOT NULL, 
    author VARCHAR(200) NOT NULL, 
    details VARCHAR(500), 
    PRIMARY KEY(book_id) 
);
CREATE TABLE user( 
    user_id INT NOT NULL AUTO_INCREMENT, 
    first_name VARCHAR(75) NOT NULL, 
    last_name VARCHAR(75) NOT NULL, 
    PRIMARY KEY(user_id) );
CREATE TABLE wishlist( 
    wishlist_id INT NOT NULL AUTO_INCREMENT, 
    user_id INT NOT NULL, book_id INT NOT NULL, 
    PRIMARY KEY(wishlist_id), 
    CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES book(book_id), 
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES user(user_id) 
);

/*
    Insert values into the Store table (1)
*/
INSERT INTO store(locale) VALUES('1 Letterman Dr, San Francisco, CA 94129');

/*
    Insert values into the Book table (9)
*/
INSERT INTO book(book_name, author, details) VALUES('Ahsoka', 'E.K.Johnston', 'Life after the Jedi Order');
INSERT INTO book(book_name, author, details) VALUES('Thrawn', 'Timothy Zahn', 'Rise to master of war');
INSERT INTO book(book_name, author) VALUES('Lords of the Sith', 'Paul S. Kemp');
INSERT INTO book(book_name, author) VALUES('Tarkin', 'James Luceno');
INSERT INTO book(book_name, author) VALUES('Most Wanted', 'Rae Carson');
INSERT INTO book(book_name, author, details) VALUES('Rebel Rising', 'Beth Revis', 'Early years of Jyn Erso');
INSERT INTO book(book_name, author) VALUES('A New Dawn', 'John Jackson Miller');
INSERT INTO book(book_name, author, details) VALUES('Lost Stars', 'Claudia Gray', 'Story of the world Jelucan');
INSERT INTO book(book_name, author, details) VALUES('Padawan', 'Kiersten White', 'Obi-wan journeys alone as a padawan');

/*
    Insert values into the User table (3) 
*/
INSERT INTO user(first_name, last_name) VALUES('Leia', 'Organa');
INSERT INTO user(first_name, last_name) VALUES('Luke', 'Skywalker');
INSERT INTO user(first_name, last_name) VALUES('Han', 'Solo');

/*
    Insert values into the Wishlist table (1 per user) 
*/
INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user
WHERE first_name = 'Leia'), (SELECT book_id FROM book WHERE book_name = 'Tarkin'));
INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user
WHERE first_name = 'Luke'), (SELECT book_id FROM book WHERE book_name = 'Lords of the Sith'));
INSERT INTO wishlist(user_id, book_id) VALUES ((SELECT user_id FROM user
WHERE first_name = 'Han'), (SELECT book_id FROM book WHERE book_name = 'Rebel Rising'));