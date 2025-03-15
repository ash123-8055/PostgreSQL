from connection import conn


cursor=conn.cursor()
cursor.commit("revoke all on employee from coder@localhost;")
conn.commit()
print("Revoked all the access on employee for coder")

cursor.commit("grant all on employee to coder@localhost;")
conn.commit()
print("Granted all the access on employee for coder")
