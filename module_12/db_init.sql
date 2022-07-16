CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

CREATE TABLE store (
    store_id    INT  NOT NULL  AUTO_INCREMENT,
    locale  ARCHAR(500)  NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

INSERT INTO store(locale)
    VALUES('550 S 16th St, Lincoln, NE 68508');

INSERT INTO book(book_name, author, details)
    VALUES('Tale of Two Cities', 'Charles Dickens', 'Story about events in London and Paris before and during the French Revolution');

INSERT INTO book(book_name, author, details)
    VALUES('Leviathan Wakes', 'S.A. Corey', 'Book 1 of the Expanse series.');

INSERT INTO book(book_name, author, details)
    VALUES('The Class', 'Erich Segal', 'Story of five Harvard Univesity Classmates');

INSERT INTO book(book_name, author)
    VALUES('Leviathan Sleeps', 'S.A. Corey', 'Book 9 of the Expanse Series.');

INSERT INTO book(book_name, author)
    VALUES('CEH v11 Exam Guide', 'Matt Walker', 'CEH test preparation guide.');

INSERT INTO book(book_name, author)
    VALUES('Seveneves', 'Neal Stephenson', 'Story set during and after destruction of life on Earth.');

INSERT INTO book(book_name, author)
    VALUES('The Martian', 'Andy Weir', 'An astronaut is stranded on Mars and must survive.');

INSERT INTO book(book_name, author)
    VALUES('Hail Mary', 'Andy Weir', 'A scientist must travel to another solar system to solve existential crisis on Earth.');

INSERT INTO book(book_name, author)
    VALUES('How to Avoid a Climate Disaster', 'Bill Gates', 'Strategies to reverse the effects of climate change.');


INSERT INTO user(first_name, last_name) 
    VALUES('Andrew', 'Cano');

INSERT INTO user(first_name, last_name)
    VALUES('Elizabeth', 'Cano');

INSERT INTO user(first_name, last_name)
    VALUES('Mary', 'Ryan');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Andrew'), 
        (SELECT book_id FROM book WHERE book_name = 'CEH v11 EXAM GUIDE')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Elizabeth'),
        (SELECT book_id FROM book WHERE book_name = 'Leviathan Wakes')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Mary'),
        (SELECT book_id FROM book WHERE book_name = 'The Martian')
    );
