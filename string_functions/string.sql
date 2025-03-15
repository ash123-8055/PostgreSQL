-- Get length of each employee's name
SELECT name, LENGTH(name) FROM employee;

-- Convert names to lowercase
SELECT name, LOWER(name) FROM employee;

-- Convert names to uppercase
SELECT name, UPPER(name) FROM employee;

-- Extract first 3 characters from names
SELECT name, SUBSTRING(name FROM 1 FOR 3) FROM employee;

-- Remove spaces from names
SELECT name, TRIM(name) FROM employee;

-- Replace 'John' with 'Jonathan' in names
SELECT name, REPLACE(name, 'John', 'Jonathan') FROM employee;

-- Concatenate name and email
SELECT CONCAT(name, ' (', email, ')') AS full_info FROM employee;

-- Concatenate with a separator
SELECT CONCAT_WS(' - ', name, email, salary) FROM employee;

-- Split email and get domain part
SELECT email, SPLIT_PART(email, '@', 2) AS domain FROM employee;

-- Find position of '@' in email
SELECT email, POSITION('@' IN email) FROM employee;
