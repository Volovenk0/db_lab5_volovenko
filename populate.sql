INSERT INTO author (author_id, author_name) VALUES (1, 'George Orwell');
INSERT INTO author (author_id, author_name) VALUES (2, 'George R. R. Martin');
INSERT INTO author (author_id, author_name) VALUES (3, 'Fredrik Backman');
INSERT INTO author (author_id, author_name) VALUES (4, 'Madeleine LEngle');
INSERT INTO author (author_id, author_name) VALUES (5, 'Ron Chernow');
INSERT INTO author (author_id, author_name) VALUES (6, 'Veronica Roth');
INSERT INTO author (author_id, author_name) VALUES (7, 'Bill Martin Jr.');
INSERT INTO author (author_id, author_name) VALUES (8, 'Charlaine Harris');
INSERT INTO author (author_id, author_name) VALUES (9, 'J.K. Rowling');
INSERT INTO author (author_id, author_name) VALUES (10, 'Paula Hawkins');

INSERT INTO book (book_id, book_name, price, rating) VALUES (1, '1984', 6, 4.7);
INSERT INTO book (book_id, book_name, price, rating) VALUES (2, 'A Dance with Dragons', 11, 4.4);
INSERT INTO book (book_id, book_name, price, rating) VALUES (3, 'A Man Called Ove', 8, 4.6);
INSERT INTO book (book_id, book_name, price, rating) VALUES (4, 'A Wrinkle in Time', 5, 4.5);
INSERT INTO book (book_id, book_name, price, rating) VALUES (5, 'Alexander Hamilton', 13, 4.8);
INSERT INTO book (book_id, book_name, price, rating) VALUES (6, 'Allegiant', 13, 3.9);
INSERT INTO book (book_id, book_name, price, rating) VALUES (7, 'Brown Bear, Brown Bear, What Do You See?', 5, 4.9);
INSERT INTO book (book_id, book_name, price, rating) VALUES (8, 'Dead Reckoning (Sookie Stackhouse/True Blood, Book 11)', 4, 4.2);
INSERT INTO book (book_id, book_name, price, rating) VALUES (9, 'The Casual Vacancy', 12, 3.3);
INSERT INTO book (book_id, book_name, price, rating) VALUES (10, 'The Girl on the Train', 18, 4.1);

INSERT INTO genre (genre_id, genre_name) VALUES (1, 'dystopian fiction');
INSERT INTO genre (genre_id, genre_name) VALUES (2, 'fantasy');
INSERT INTO genre (genre_id, genre_name) VALUES (3, 'fiction');
INSERT INTO genre (genre_id, genre_name) VALUES (4, 'biography');
INSERT INTO genre (genre_id, genre_name) VALUES (5, 'science fiction');
INSERT INTO genre (genre_id, genre_name) VALUES (6, 'childrens Literature');
INSERT INTO genre (genre_id, genre_name) VALUES (7, 'thriller');

INSERT INTO book_genre (book_id, genre_id) VALUES (1, 1);
INSERT INTO book_genre (book_id, genre_id) VALUES (2, 2);
INSERT INTO book_genre (book_id, genre_id) VALUES (3, 3);
INSERT INTO book_genre (book_id, genre_id) VALUES (4, 2);
INSERT INTO book_genre (book_id, genre_id) VALUES (5, 4);
INSERT INTO book_genre (book_id, genre_id) VALUES (6, 5);
INSERT INTO book_genre (book_id, genre_id) VALUES (7, 6);
INSERT INTO book_genre (book_id, genre_id) VALUES (8, 2);
INSERT INTO book_genre (book_id, genre_id) VALUES (9, 2);
INSERT INTO book_genre (book_id, genre_id) VALUES (10, 7);

INSERT INTO book_author (book_id, author_id) VALUES (1, 1);
INSERT INTO book_author (book_id, author_id) VALUES (2, 2);
INSERT INTO book_author (book_id, author_id) VALUES (3, 3);
INSERT INTO book_author (book_id, author_id) VALUES (4, 4);
INSERT INTO book_author (book_id, author_id) VALUES (5, 5);
INSERT INTO book_author (book_id, author_id) VALUES (6, 6);
INSERT INTO book_author (book_id, author_id) VALUES (7, 7);
INSERT INTO book_author (book_id, author_id) VALUES (8, 8);
INSERT INTO book_author (book_id, author_id) VALUES (9, 9);
INSERT INTO book_author (book_id, author_id) VALUES (10, 10);

