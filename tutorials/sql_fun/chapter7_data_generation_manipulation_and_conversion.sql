CREATE TABLE string_tbl
(char_fld CHAR(30),
vchar_fld VARCHAR(30),
text_fld TEXT
);

INSERT INTO string_tbl (char_fld, vchar_fld, text_fld)
VALUES ('This is char data',
'This is varchar data',
'This is text data');

SELECT * FROM string_tbl;


SELECT quote(text_fld) FROM string_tbl;

SELECT 'abcdefg', CHAR(97,98,99,100,101,102,103 USING utf8mb4);

# this one doesn't work
SELECT CONCAT('danke sch', CHAR(195 USING utf8mb4), 'n');

SELECT CHAR(77,121,83,81,'76' USING utf8mb4);

SELECT ASCII('ö');



# Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.
# Better do that from command line
DELETE FROM string_tbl;



INSERT INTO string_tbl (char_fld, vchar_fld, text_fld)
VALUES ('This string is 28 characters',
'This string is 28 characters',
'This string is 28 characters');

SELECT LENGTH(char_fld) char_length,
LENGTH(vchar_fld) varchar_length,
LENGTH(text_fld) text_length
FROM string_tbl;

SELECT POSITION('characters' IN vchar_fld)
FROM string_tbl;


SELECT concat(first_name, ' ', last_name,
    ' has been a customer since ', date(create_date)) cust_narrative
FROM customer;

SELECT POW(2,10) kilobyte, POW(2,20) megabyte,
POW(2,30) gigabyte, POW(2,40) terabyte;


SELECT @@global.time_zone, @@session.time_zone;
