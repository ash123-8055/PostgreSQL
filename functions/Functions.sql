-- CREATE TABLE employee (
--     id varchar(20),
--     name VARCHAR(100),
--     email VARCHAR(100),
--     salary int,
-- 	primary key(id)
-- );

-- INSERT INTO employee (id, name, email, salary) VALUES
-- ('E001', 'John Doe', 'john.doe@example.com', 50000),
-- ('E002', 'Jane Smith', 'jane.smith@example.com', 60000),
-- ('E003', 'Alice Johnson', 'alice.johnson@example.com', 55000),
-- ('E004', 'Bob Williams', 'bob.williams@example.com', 58000),
-- ('E005', 'Charlie Brown', 'charlie.brown@example.com', 62000);

-- select * from employee;

-- Count total employees
SELECT COUNT(*) FROM employee;

-- Total salary of all employees
SELECT SUM(salary) FROM employee;

-- Average salary
SELECT AVG(salary) FROM employee;

-- Minimum salary
SELECT MIN(salary) FROM employee;

-- Maximum salary
SELECT MAX(salary) FROM employee;

-- Concatenate all employee names
SELECT STRING_AGG(name, ', ') FROM employee;

-- Collect employee names into an array
SELECT ARRAY_AGG(name) FROM employee;

-- Median salary (percentile 50%)
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employee;

-- Variance in salary distribution
SELECT VARIANCE(salary) FROM employee;

-- Standard deviation of salaries
SELECT STDDEV(salary) FROM employee;
