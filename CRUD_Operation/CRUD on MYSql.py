from connection import conn


cursor=conn.cursor()
#creating a table
cursor.execute("Create table employee(id varchar(10),fname varchar(20),lname varchar(20),primary key(id));")
conn.commit()

#Inserting values into the table
cursor.execute("insert into employee values('1','Ash','Kum'),('2','A','K'),('3','Po','Lo');")
conn.commit()
print("Data has been inserted")

#selecting from the table
print("Data inside the table as follows:")
cursor.execute("select * from employee;")
row=cursor.fetchall()
for rows in row:
    print(row)

#updating values in the table
cursor.execute("update employee set lname='kum' where id='2';")
conn.commit()
cursor.execute("select * from employee;")
row=cursor.fetchall()
print("Updated table as follows: ")
for rows in row:
    print(row)

#deleting values from the table
cursor.execute("delete from employee where id=1;")
conn.commit()
cursor.execute("select * from employee;")
row=cursor.fetchall()
print("table after deletion: ")
for rows in row:
    print(row)
