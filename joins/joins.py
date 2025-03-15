from connection import conn


cursor=conn.cursor()

print("\nInner Join\n")
cursor.execute("SELECT table1.id, table1.name, table1.age, table2.city, table2.country FROM table1 INNER JOIN table2 ON table1.id = table2.id;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nLeft Join\n")
cursor.execute("SELECT table1.id, table1.name, table1.age, table2.city, table2.country FROM table1 LEFT JOIN table2 ON table1.id = table2.id;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nRight Join\n")
cursor.execute("SELECT table1.id, table1.name, table1.age, table2.city, table2.country FROM table1 RIGHT JOIN table2 ON table1.id = table2.id;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nFULL OUTER Join\n")
cursor.execute("SELECT table1.id, table1.name, table1.age, table2.city, table2.country FROM table1 FULL OUTER JOIN table2 ON table1.id = table2.id;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nCross Join\n")
cursor.execute("SELECT table1.id, table1.name, table1.age, table2.city, table2.country FROM table1 CROSS JOIN table2 ")
rows=cursor.fetchall()
for row in rows:
    print(row)



