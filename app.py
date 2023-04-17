import sqlite3


conn =sqlite3.connect('customer.db')

cursor= conn.cursor()

#Drop or delete the table
cursor.execute("DROP TABLE customers")
conn.commit()




#query the database
cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()


for item in items:
    print(item)

conn.close()