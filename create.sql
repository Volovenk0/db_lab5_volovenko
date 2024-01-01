CREATE TABLE Book
(
  book_id INT NOT NULL,
  book_name VARCHAR(200) NOT NULL,
  price INT NOT NULL,
  rating FLOAT NOT NULL,
  PRIMARY KEY (book_id)
);

CREATE TABLE Author
(
  author_id INT NOT NULL,
  author_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (author_id)
);

CREATE TABLE Genre
(
  genre_id INT NOT NULL,
  genre_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (genre_id)
);

CREATE TABLE book_author
(
  author_id INT NOT NULL,
  book_id INT NOT NULL,
  PRIMARY KEY (author_id, book_id),
  FOREIGN KEY (author_id) REFERENCES Author(author_id),
  FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE book_genre
(
  book_id INT NOT NULL,
  genre_id INT NOT NULL,
  PRIMARY KEY (book_id, genre_id),
  FOREIGN KEY (book_id) REFERENCES Book(book_id),
  FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);