from connection import conn

cursor = conn.cursor()

print("\nGet the current timestamp\n")
cursor.execute("SELECT NOW();")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nGet the current date\n")
cursor.execute("SELECT CURRENT_DATE;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nExtract year from hire date\n")
cursor.execute("SELECT hire_date, EXTRACT(YEAR FROM hire_date) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nCalculate employee tenure (difference from today)\n")
cursor.execute("SELECT name, AGE(hire_date) AS tenure FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nExtract month from hire date\n")
cursor.execute("SELECT hire_date, DATE_PART('month', hire_date) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nRound hire date to nearest month\n")
cursor.execute("SELECT hire_date, DATE_TRUNC('month', hire_date) FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nFormat hire date as 'YYYY-MM-DD'\n")
cursor.execute("SELECT hire_date, TO_CHAR(hire_date, 'YYYY-MM-DD') FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nAdd 5 days to hire date\n")
cursor.execute("SELECT hire_date, hire_date + INTERVAL '5 days' FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nAdd 1 month to hire date\n")
cursor.execute("SELECT hire_date, hire_date + INTERVAL '1 month' FROM employee;")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nNormalize interval (e.g., 13 months → 1 year + 1 month)\n")
cursor.execute("SELECT JUSTIFY_INTERVAL(INTERVAL '13 months');")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
