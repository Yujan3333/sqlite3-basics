import sqlite3


conn =sqlite3.connect('customer.db')

cursor= conn.cursor()

#query the database -- Order by
cursor.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

items = cursor.fetchall()


for item in items:
    print(item)

conn.close()