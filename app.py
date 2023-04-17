import sqlite3

# conn = sqlite3.connect(':memory:')

# making a connection with the database
conn =sqlite3.connect('customer.db')

# cursor tells the db what you want to do?
cursor= conn.cursor()

# create a table
# here 3 quotation(""") marks is the docs string
cursor.execute(""" CREATE TABLE customers (
    first_name text,
    last_name text,
    email  text
    )""")

# sqlite3 has 5 datatypes:= NULL, INTEGER, REAL, TEXT, BLOB

# commit to db
conn.commit()

#Close your connection
conn.close()