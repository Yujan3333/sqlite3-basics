import sqlite3


conn =sqlite3.connect('customer.db')

cursor= conn.cursor()


#delete Records
cursor.execute("DELETE from customers WHERE rowid=3 ")

#commit to the db
conn.commit()

#query the database
cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()


for item in items:
    print(item)

conn.close()