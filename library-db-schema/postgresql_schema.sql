-- PostgreSQL Schema for Library Database

DROP SCHEMA IF EXISTS library CASCADE; 
CREATE SCHEMA library;
SET search_path TO library;

CREATE TABLE library.users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE library.authors (
    author_id SERIAL PRIMARY KEY,
    user_id INT UNIQUE,
    name VARCHAR(255) NOT NULL,
    biography TEXT,
    nationality VARCHAR(100),
    birth_date DATE,
    death_date DATE,
    FOREIGN KEY (user_id) REFERENCES library.users(user_id) ON DELETE SET NULL
);

CREATE TABLE library.genres (
    genre_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE library.books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publication_year INT,
    isbn VARCHAR(20) UNIQUE,
    pages INT,
    language VARCHAR(50),
    publisher VARCHAR(255)
);

CREATE TABLE library.book_authors (
    book_author_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    author_id INT NOT NULL,
    contribution VARCHAR(100),
    FOREIGN KEY (book_id) REFERENCES library.books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES library.authors(author_id) ON DELETE CASCADE
);

CREATE TABLE library.book_genres (
    book_genre_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    genre_id INT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES library.books(book_id) ON DELETE SET NULL,
    FOREIGN KEY (genre_id) REFERENCES library.genres(genre_id) ON DELETE CASCADE
);

CREATE TABLE library.book_copies (
    copy_id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    status VARCHAR(50) DEFAULT 'available',
    condition VARCHAR(100),
    acquisition_date DATE,
    location VARCHAR(255),
    FOREIGN KEY (book_id) REFERENCES library.books(book_id) ON DELETE CASCADE
);

CREATE TABLE library.reservations (
    reservation_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    copy_id INT NOT NULL,
    reservation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    due_date DATE,
    return_date TIMESTAMP,
    status VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES library.users(user_id) ON DELETE SET NULL,
    FOREIGN KEY (copy_id) REFERENCES library.book_copies(copy_id) ON DELETE SET NULL
);