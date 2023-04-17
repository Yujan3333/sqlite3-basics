import sqlite3


conn =sqlite3.connect('customer.db')

cursor= conn.cursor()

# python list of customer with tuple 
many_customers =[
                    ('Chris','Ronaldo','chris@gmail.com'),
                    ('Deku','Midoria','deku@gmail.com'),
                    ('Naruto','Uzumaki','naruto@gmail.com')
                ]


#executemany
cursor.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

print("Command Executed")

conn.commit()

conn.close()