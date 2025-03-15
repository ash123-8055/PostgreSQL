from connection import conn


cursor=conn.cursor()

cursor.execute("""
CREATE FUNCTION get_name(emp_id VARCHAR)
RETURNS CHAR
LANGUAGE SQL
AS $$
    SELECT name FROM employee WHERE id = emp_id;
$$;
""")

cursor.execute("SELECT get_name('E002')")
rows=cursor.fetchall()
for row in rows:
    print(row)