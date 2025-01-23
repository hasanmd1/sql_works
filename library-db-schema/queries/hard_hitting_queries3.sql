-- Find Books That Have Never Been Reserved

SELECT b.book_id, b.title
FROM library.books b
INNER JOIN library.book_copies bc ON b.book_id = bc.book_id
LEFT JOIN library.reservations r ON bc.copy_id = r.copy_id
WHERE r.reservation_id IS NULL;
