from connection import conn


cursor=conn.cursor()
cursor.execute("create table employee(id varchar(10),fname varchar(30),lname varchar(30),age int,Primary Key(id));")
conn.commit()
print("Created the table")

cursor.execute("alter table employee add column salary int;")
conn.commit()
print("Added a new column 'salary'")

cursor.execute("truncate table employee;")
conn.commit()
print("Truncated the table.. No values in the table")

