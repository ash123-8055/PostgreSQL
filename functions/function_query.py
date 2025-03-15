from connection import conn

cursor = conn.cursor()

print("\nCount total employees\n")
cursor.execute("SELECT COUNT(*) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nTotal salary of all employees\n")
cursor.execute("SELECT SUM(salary) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nAverage salary\n")
cursor.execute("SELECT AVG(salary) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nMinimum salary\n")
cursor.execute("SELECT MIN(salary) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nMaximum salary\n")
cursor.execute("SELECT MAX(salary) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nConcatenate all employee names\n")
cursor.execute("SELECT STRING_AGG(name, ', ') FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nCollect employee names into an array\n")
cursor.execute("SELECT ARRAY_AGG(name) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nMedian salary (percentile 50%)\n")
cursor.execute("SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nVariance in salary distribution\n")
cursor.execute("SELECT VARIANCE(salary) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nStandard deviation of salaries\n")
cursor.execute("SELECT STDDEV(salary) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
