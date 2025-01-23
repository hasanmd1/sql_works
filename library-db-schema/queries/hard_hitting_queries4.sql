-- Find Authors Who Have Written at Least 2 Books

SELECT a.author_id, a.name, COUNT(DISTINCT ba.book_id) AS book_count
FROM library.authors a
INNER JOIN library.book_authors ba ON a.author_id = ba.author_id
GROUP BY a.author_id, a.name
HAVING COUNT(DISTINCT ba.book_id) >= 2;
