SELECT c.first_name, c.last_name, a.address
FROM customer c JOIN address a; # a lot of values as it is Cartesian product

SELECT c.first_name, c.last_name, a.address
FROM customer c JOIN address a
    ON c.address_id = a.address_id;
    
SELECT c.first_name, c.last_name, a.address
FROM customer c INNER JOIN address a
    ON c.address_id = a.address_id;
    
    
# as botth columns have same name USING can be used
SELECT c.first_name, c.last_name, a.address
FROM customer c INNER JOIN address a
    USING (address_id);
    
# OLDY syntax
SELECT c.first_name, c.last_name, a.address
FROM customer c, address a
WHERE c.address_id = a.address_id;



SELECT c.first_name, c.last_name, a.address
FROM customer c, address a
WHERE c.address_id = a.address_id
    AND a.postal_code = 52137;
    
SELECT c.first_name, c.last_name, a.address
FROM customer c INNER JOIN address a
    ON c.address_id = a.address_id
WHERE a.postal_code = 52137;


SELECT c.first_name, c.last_name, ct.city
FROM customer c 
    INNER JOIN address a
    ON c.address_id = a.address_id
    INNER JOIN city ct
    ON a.city_id = ct.city_id;
    
    
SELECT STRAIGHT_JOIN c.first_name, c.last_name, ct.city
FROM city ct
    INNER JOIN address a
    ON a.city_id = ct.city_id
    INNER JOIN customer c
    ON c.address_id = a.address_id;
    
# using subqueries as tables
SELECT c.first_name, c.last_name, addr.address, addr.city
FROM customer c
    INNER JOIN
        (SELECT a.address_id, a.address, ct.city
        FROM address as a
            INNER JOIN city ct
            ON a.city_id = ct.city_id
        WHERE a.district = 'California'
        ) addr
    ON c.address_id = addr.address_id;
    
# Using same table twice
SELECT f.title
FROM film f
    INNER JOIN film_actor fa
    ON f.film_id = fa.film_id
    INNER JOIN actor a
    ON fa.actor_id = a.actor_id
WHERE (
        (a.first_name = 'CATE' AND a.last_name = 'MCQUEEN')
        OR (a.first_name = 'CUBA' AND a.last_name = 'BIRCH')
    );

# Using same table twice
SELECT f.title
FROM film f
    INNER JOIN film_actor fa1
    ON f.film_id = fa1.film_id
    INNER JOIN actor a1
    ON fa1.actor_id = a1.actor_id
    INNER JOIN film_actor fa2
    ON f.film_id = fa2.film_id
    INNER JOIN actor a2
    ON fa2.actor_id = a2.actor_id
WHERE (
        (a1.first_name = 'CATE' AND a1.last_name = 'MCQUEEN')
        AND (a2.first_name = 'CUBA' AND a2.last_name = 'BIRCH')
    );
    
# SELF-JOINS
# this will not work
SELECT f.title, f_prnt.title prequel
	FROM film f
	INNER JOIN film f_prnt
	ON f_prnt.film_id = f.prequel_film_id
WHERE f.prequel_film_id IS NOT NULL;

# TASKS 
SELECT c.first_name, c.last_name, a.address, ct.city
FROM customer c
    INNER JOIN address a
    ON c.address_id = a.address_id
    INNER JOIN city ct
    ON a.city_id = ct.city_id
WHERE a.district = 'California';



SELECT f.title
FROM film f
    INNER JOIN film_actor fa
    ON f.film_id = fa.film_id
    INNER JOIN actor a
    ON fa.actor_id = a.actor_id
WHERE a.first_name = 'JOHN';


SELECT DISTINCT ct.city, a1.address address1, a2.address address2
FROM address a1
    INNER JOIN address a2
    ON a1.city_id = a2.city_id
    INNER JOIN city ct
    ON ct.city_id = a1.city_id
WHERE a1.address != a2.address
ORDER BY ct.city;

