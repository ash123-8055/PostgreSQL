from connection import conn


cursor=conn.cursor()

cursor.execute("""
CREATE PROCEDURE add_salary(emp_id varchar(20))
LANGUAGE SQL
AS $$
UPDATE employee 
SET salary=salary+1000
where id = emp_id
$$;
""")

#Call the procedure which updates the values
cursor.execute("CALL add_salary('E001');")

cursor.execute("select * from employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\n")

cursor.execute("CALL add_salary('E001');")

cursor.execute("select * from employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)
