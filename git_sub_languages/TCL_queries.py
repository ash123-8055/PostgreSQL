from connection import conn


cursor=conn.cursor()
conn.start_transaction()
cursor.execute("delete from employee;")
conn.commit()

cursor.execute("insert into employee(id,fname,lname,age) values('1','Ash','K',20),('2','Ashwin','Kumar',21),('3','A','K',22);")
conn.commit()
print("Inserted 3 rows into the table")

cursor.execute("select * from employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SAVEPOINT before_updation;")

cursor.execute("update employee set age=30 where id='1';")
print("Updated the values in table")

cursor.execute("ROLLBACK to before_updation")
print("Rollback before updation")
cursor.execute("select * from employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SAVEPOINT before_deletion;")

cursor.execute("delete from employee where id='3';")
print("Deleted some values in the table")

cursor.execute("ROLLBACK to before_deletion")
print("Rollback to before Deletion")
cursor.execute("select * from employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

