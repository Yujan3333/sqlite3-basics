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
cursor.execute("SELECT * FROM customers")

# cursor.fetchone()
# cursor.fetchmany(3)

#create a variable to hold the fetched data
items = cursor.fetchall()

print("Name\t\t\tEmail")
for item in items:
    print(item[0]+' '+item[1]+"\t\t"+item[2])
    



print("Command Executed")

conn.commit()

conn.close()