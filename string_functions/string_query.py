from connection import conn


cursor=conn.cursor()

print("\nGet length of each employee's name\n")
cursor.execute("SELECT name, LENGTH(name) FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nConvert names to lowercase\n")
cursor.execute("SELECT name, LOWER(name) FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nConvert names to uppercase\n")
cursor.execute("SELECT name, UPPER(name) FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nExtract first 3 characters from names\n")
cursor.execute("SELECT name, SUBSTRING(name FROM 1 FOR 3) FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nRemove spaces from names\n")
cursor.execute("SELECT name, TRIM(name) FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nReplace 'John' with 'Jonathan' in names\n")
cursor.execute("SELECT name, REPLACE(name, 'John', 'Jonathan') FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nConcatenate name and email\n")
cursor.execute("SELECT CONCAT(name, ' (', email, ')') AS full_info FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nConcatenate with a separator\n")
cursor.execute("SELECT CONCAT_WS(' - ', name, email, salary) FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nSplit email and get domain part\n")
cursor.execute("SELECT email, SPLIT_PART(email, '@', 2) AS domain FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)

print("\nFind position of '@' in email\n")
cursor.execute("SELECT email, POSITION('@' IN email) FROM employee;")
rows=cursor.fetchall()
for row in rows:
    print(row)