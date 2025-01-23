-- List All Books Along with Their Authors and Genres

SELECT 
    b.book_id, 
    b.title, 
    STRING_AGG(DISTINCT a.name, ', ') AS authors, 
    STRING_AGG(DISTINCT g.name, ', ') AS genres
FROM library.books b
LEFT JOIN library.book_authors ba ON b.book_id = ba.book_id
LEFT JOIN library.authors a ON ba.author_id = a.author_id
LEFT JOIN library.book_genres bg ON b.book_id = bg.book_id
LEFT JOIN library.genres g ON bg.genre_id = g.genre_id
GROUP BY b.book_id, b.title
ORDER BY b.title;
