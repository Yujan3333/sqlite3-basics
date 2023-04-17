import sqlite3


conn =sqlite3.connect('customer.db')

cursor= conn.cursor()


#update Records
cursor.execute("UPDATE customers SET first_name ='Yujan' WHERE rowid=1 ")

#commit to the db
conn.commit()

#query the database
cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()


for item in items:
    print(item)

conn.close()