CREATE FUNCTION get_salary(emp_id VARCHAR)
RETURNS NUMERIC
LANGUAGE SQL
AS $$
    SELECT salary FROM employee WHERE id = emp_id;
$$;

SELECT get_salary('E001')
