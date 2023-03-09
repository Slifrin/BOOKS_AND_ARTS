SELECT customer_id, COUNT(*) number
FROM rental
GROUP BY customer_id
ORDER BY number DESC;


SELECT customer_id, COUNT(*) number
FROM rental
GROUP BY customer_id
HAVING number >= 40
ORDER BY number;



SELECT MAX(amount) max_amt,
    MIN(amount) min_amt,
    AVG(amount) avg_amt,
    SUM(amount) tot_amt,
    COUNT(*) num_payments
FROM payment;


SELECT customer_id,
    MAX(amount) max_amt,
    MIN(amount) min_amt,
    AVG(amount) avg_amt,
    SUM(amount) tot_amt,
    COUNT(*) num_payments
FROM payment
GROUP BY customer_id;


SELECT COUNT(customer_id) num_rows,
COUNT(DISTINCT customer_id) num_customers
FROM payment;


# using expressions
SELECT MAX(DATEDIFF(return_date,rental_date))
FROM rental;

# Multicolumn Grouping
SELECT fa.actor_id, f.rating, COUNT(*)
FROM film_actor fa
    INNER JOIN film f 
    ON fa.film_id = f.film_id
GROUP BY fa.actor_id, f.rating
ORDER BY 1,2;


# Grouping via Expression
SELECT extract(YEAR FROM rental_date) year, COUNT(*) how_many
FROM rental
GROUP BY extract(YEAR FROM rental_date);


# Generating Rollups
SELECT fa.actor_id, f.rating, COUNT(*)
FROM film_actor fa
    INNER JOIN film f 
    ON fa.film_id = f.film_id
GROUP BY fa.actor_id, f.rating WITH ROLLUP
ORDER BY 1,2;

SELECT fa.actor_id, f.rating, COUNT(*)
FROM film_actor fa
    INNER JOIN film f
    ON fa.film_id = f.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY fa.actor_id, f.rating
HAVING count(*) > 9;


# TASKS
SELECT COUNT(*)
FROM payment;


SELECT customer_id, COUNT(*), SUM(amount)
FROM payment
GROUP BY customer_id;


SELECT customer_id, SUM(amount), COUNT(amount) payment_with_amount
FROM payment
GROUP BY customer_id
HAVING payment_with_amount >= 40;

SELECT customer_id, SUM(amount), COUNT(*) payment_with_amount
FROM payment
GROUP BY customer_id
HAVING payment_with_amount >= 40;





