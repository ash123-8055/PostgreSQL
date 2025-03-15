from connection import conn


cursor=conn.cursor()

cursor.execute("""
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY NOT NULL,
   NAME TEXT NOT NULL,
   AGE INT NOT NULL,
   ADDRESS CHAR(50),
   SALARY REAL
);
""")

cursor.execute("""
CREATE TABLE AUDIT(
   EMP_ID INT NOT NULL,
   ENTRY_DATE TEXT NOT NULL
);
""")

#Creating a trigger function which works after the trigger is launched
cursor.execute("""
CREATE OR REPLACE FUNCTION auditlog() RETURNS TRIGGER AS $$
BEGIN
   INSERT INTO AUDIT(EMP_ID, ENTRY_DATE) VALUES (NEW.ID, current_timestamp);
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;
""")

#Trigger which works after the insertion on table COMPANY
cursor.execute("""
CREATE TRIGGER example_trigger 
AFTER INSERT ON COMPANY
FOR EACH ROW 
EXECUTE FUNCTION auditlog();
""")

cursor.execute("""
INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY)
VALUES (1, 'Raju', 25, 'New-Delhi', 33000.00 );
""")

cursor.execute("SELECT * FROM COMPANY;")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT * FROM AUDIT;")
rows=cursor.fetchall()
for row in rows:
    print(row)