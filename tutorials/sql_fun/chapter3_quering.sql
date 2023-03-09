USE sakila;

SHOW tables;

desc customer;

SELECT language_id,
    'COMMON' language_usage,
    language_id * 3.1415927 lang_pi_value,
    upper(name) language_name
FROM language;

SELECT version(), user(), database();

SELECT language_id,
    'COMMON' AS language_usage,
    language_id * 3.1415927 AS lang_pi_value,
    upper(name) AS language_name
FROM language;

SELECT actor_id FROM film_actor ORDER BY actor_id;

SELECT DISTINCT actor_id FROM film_actor ORDER BY actor_id;



SELECT concat(cust.last_name, ', ', cust.first_name) full_name
FROM
(
	SELECT first_name, last_name, email
	FROM customer
	WHERE first_name = 'JESSIE'
) cust;


CREATE TEMPORARY TABLE actors_j
	(actor_id smallint(5),
	first_name varchar(45),
	last_name varchar(45)
);

INSERT INTO actors_j
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE 'J%';

CREATE VIEW cust_vw AS
SELECT customer_id, first_name, last_name, active
FROM customer;

SELECT first_name, last_name
FROM cust_vw
WHERE active = 0;


SELECT customer.first_name, customer.last_name,
    time(rental.rental_date) rental_time
    FROM customer
        INNER JOIN rental
        ON customer.customer_id = rental.customer_id
WHERE date(rental.rental_date) = '2005-06-14';

SELECT c.first_name, c.last_name,
	time(r.rental_date) rental_time
FROM customer AS c
	INNER JOIN rental AS r
	ON c.customer_id = r.customer_id
WHERE date(r.rental_date) = '2005-06-14';

SELECT title 
FROM film
WHERE rating = 'G' AND rental_duration >= 7;

SELECT title 
FROM film
WHERE (rating = 'G' AND rental_duration >= 7) 
    OR (rating = 'PG-13' AND rental_duration < 4);
    
    
    
    
SELECT c.first_name, c.last_name, count(*)
FROM customer AS c
    INNER JOIN rental AS r
    ON c.customer_id = r.customer_id
GROUP BY c.first_name, c.last_name
HAVING count(*) >= 40;

SELECT c.first_name, c.last_name, count(*)
FROM customer AS c
    INNER JOIN rental AS r
    ON c.customer_id = r.customer_id
GROUP BY c.first_name, c.last_name
HAVING count(*) >= 40
ORDER BY count(*) DESC;


SELECT c.first_name, c.last_name, time(r.rental_date) rental_time
FROM customer c
    INNER JOIN rental r
    ON c.customer_id = r.customer_id
WHERE date(r.rental_dat) = '2005-06-14';

SELECT c.first_name, c.last_name, time(r.rental_date) rental_time
FROM customer c
    INNER JOIN rental r
    ON c.customer_id = r.customer_id
WHERE date(r.rental_date) = '2005-06-14'
ORDER BY time(r.rental_date) desc;

SELECT c.first_name, c.last_name, time(r.rental_date) rental_time
FROM customer c
    INNER JOIN rental r
    ON c.customer_id = r.customer_id
WHERE date(r.rental_date) = '2005-06-14'
ORDER BY 3 desc;
