CREATE PROCEDURE add_salary(emp_id varchar(20))
LANGUAGE SQL
AS $$
UPDATE employee 
SET salary=salary+1000
where id = emp_id
$$;

select * from employee;

CALL add_salary('E001');

