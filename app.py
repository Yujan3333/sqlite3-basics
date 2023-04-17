import sqlite3


conn =sqlite3.connect('customer.db')

cursor= conn.cursor()

#query the database -- AND , OR, LIKE
cursor.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'M%' OR rowid =1")

items = cursor.fetchall()


for item in items:
    print(item)

conn.close()