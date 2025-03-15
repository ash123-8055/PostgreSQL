from connection import conn

cursor = conn.cursor()

cursor.execute("create index idx_name1 on table1(name)")
cursor.execute("create index idx_name_age1 on table1(name,age)")
cursor.execute("select * from pg_indexes where tablename='table1';")
rows=cursor.fetchall()
for row in rows:
    print(row)