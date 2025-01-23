-- Find Users Who Have Reserved Books But Have Never Borrowed a Copy

SELECT DISTINCT u.user_id, u.name, u.email
FROM library.users u
INNER JOIN library.reservations r ON u.user_id = r.user_id
WHERE r.return_date IS NULL;
