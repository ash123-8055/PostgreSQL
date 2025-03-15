-- ALTER TABLE employee ADD COLUMN hire_date DATE;
-- UPDATE employee SET hire_date = '2022-03-15' WHERE id = 'E001';
-- UPDATE employee SET hire_date = '2021-07-10' WHERE id = 'E002';
-- UPDATE employee SET hire_date = '2020-11-25' WHERE id = 'E003';
-- UPDATE employee SET hire_date = '2019-05-30' WHERE id = 'E004';
-- UPDATE employee SET hire_date = '2023-01-12' WHERE id = 'E005';




-- Get the current timestamp
SELECT NOW();

-- Get the current date
SELECT CURRENT_DATE;

-- Extract year from hire date
SELECT hire_date, EXTRACT(YEAR FROM hire_date) FROM employee;

-- Calculate employee tenure (difference from today)
SELECT name, AGE(hire_date) AS tenure FROM employee;

-- Extract month from hire date
SELECT hire_date, DATE_PART('month', hire_date) FROM employee;

-- Round hire date to nearest month
SELECT hire_date, DATE_TRUNC('month', hire_date) FROM employee;

-- Format hire date as 'YYYY-MM-DD'
SELECT hire_date, TO_CHAR(hire_date, 'YYYY-MM-DD') FROM employee;

-- Add 5 days to hire date
SELECT hire_date, hire_date + INTERVAL '5 days' FROM employee;

-- Add 1 month to hire date
SELECT hire_date, hire_date + INTERVAL '1 month' FROM employee;

-- Normalize interval (e.g., 13 months → 1 year + 1 month)
SELECT JUSTIFY_INTERVAL(INTERVAL '13 months');
