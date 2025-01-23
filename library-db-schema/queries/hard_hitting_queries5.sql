-- Find Books That Belong to a Genre but Not to Another

SELECT b.book_id, b.title
FROM library.books b
INNER JOIN library.book_genres bg ON b.book_id = bg.book_id
INNER JOIN library.genres g ON bg.genre_id = g.genre_id
WHERE g.name = 'Romance'
MINUS -- use 'EXCEPT' in PostgreSQL and 'MINUS' in Oracle or MySQL
SELECT b.book_id, b.title
FROM library.books b
INNER JOIN library.book_genres bg ON b.book_id = bg.book_id
INNER JOIN library.genres g ON bg.genre_id = g.genre_id
WHERE g.name = 'Fantasy';
