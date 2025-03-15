from connection import conn


cursor=conn.cursor()
cursor.execute("insert into employee(id,fname,lname,age) values('1','Ash','K',20),('2','Ashwin','Kumar',21),('3','A','K',22);")
conn.commit()
print("Inserted 3 rows into the table")

rows=cursor.execute("select * from employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("update employee set age=30 where id='1';")
conn.commit()
print("Updated the values in table")

print("Table after updation")
cursor.execute("select * from employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("delete from employee where id='3';")
conn.commit()
print("Deleted some values in the table")

print("Table after Deletion")
cursor.execute("select * from employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

