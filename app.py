import sqlite3


conn =sqlite3.connect('customer.db')

cursor= conn.cursor()

#query the database -- LIMIT
cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

items = cursor.fetchall()


for item in items:
    print(item)

conn.close()