

SELECT DISTINCT c.email
FROM customer c 
    INNER JOIN rental r
    ON c.customer_id = r.customer_id
WHERE date(r.rental_date) <> '2005-06-14';


SELECT * FROM rental
WHERE year(rental_date) = 2004;


SELECT customer_id, rental_date
FROM rental
WHERE rental_date <= '2005-06-16'
    AND rental_date >= '2005-06-14';

SELECT customer_id, rental_date
FROM rental
WHERE rental_date BETWEEN '2005-06-14' AND '2005-06-16';

SELECT customer_id, payment_date, amount
FROM payment
WHERE amount BETWEEN 10.0 AND 11.99;

SELECT last_name, first_name
FROM customer
WHERE last_name BETWEEN 'FA' AND 'FR';


SELECT title, rating
FROM film
WHERE rating IN ('G', 'PG');

SELECT title, rating
FROM film
WHERE rating IN (SELECT rating FROM film WHERE title LIKE '%PET%');

SELECT title, rating
FROM film
WHERE rating IN (SELECT rating FROM film WHERE title LIKE '%PET%');


SELECT last_name, first_name
FROM customer
WHERE left(last_name, 1) = 'Q';



SELECT last_name, first_name
FROM customer
WHERE last_name LIKE '_A_T%S';

SELECT last_name, first_name
FROM customer
WHERE last_name LIKE 'Q%' OR last_name LIKE 'Y%';


SELECT last_name, first_name
FROM customer
WHERE last_name REGEXP '^[QY]';


SELECT rental_id, customer_id
FROM rental
WHERE return_date IS NULL;


SELECT rental_id, customer_id, return_date
FROM rental
WHERE return_date IS NULL
    OR return_date NOT BETWEEN '2005-05-01' AND '2005-09-01';
    
SELECT * FROM payment
WHERE amount IN (1.98, 7.98, 9.98);

SELECT last_name, first_name FROM customer
WHERE last_name REGEXP '^.A(.*W.*)';

SELECT last_name, first_name FROM customer
WHERE last_name LIKE '_A%W%';




