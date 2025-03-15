from connection import conn


cursor=conn.cursor()

cursor.execute("create view salary_table1 as select * from employee where salary>=60000;")

cursor.execute("create view sample1 as select table1.id as table1_id, name,city,country from table1 join table2 on table1.id=table2.id where table1.id in (1,3,5);")


print("\nSimple View\n")
cursor.execute("select * from salary_table1")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nComplex View\n")
cursor.execute("select * from sample1")
rows=cursor.fetchall()
for row in rows:
    print(row)