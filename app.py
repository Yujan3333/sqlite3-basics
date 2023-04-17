import sqlite3


conn =sqlite3.connect('customer.db')

cursor= conn.cursor()

cursor.execute("INSERT INTO customers VALUES ('Leo','Messi','Leo@gmail.com')")

print("Command Executed")

conn.commit()

conn.close()