import sqlite3


#function to show the data in database
def show_all():
    #conncetion to the db
    conn =sqlite3.connect('customer.db')

    # Create a cursor
    cursor= conn.cursor()
    
    #query the table
    cursor.execute("SELECT rowid, * FROM customers")

    # cursor.fetchone()
    # cursor.fetchmany(3)

    # creating a variable to store all data
    items=cursor.fetchall()

    for item in items:
        print(item)
    #commiting to the db
    conn.commit()
    #CLose the connection
    conn.close()
    

#ADD a new Record to the Table "customers"
def add_one_record (first,last,email):
    conn =sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
    conn.commit()
    conn.close()
    

def add_many_record(list):
    conn =sqlite3.connect('customer.db')
    c= conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)",(list))
    conn.commit()
    conn.close()


def delete_one_record(id):
    conn =sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute("DELETE from customers WHERE rowid= (?)",id)
    conn.commit()
    conn.close()
    

#Using WHERE to lookup
def email_lookup(email):
    conn =sqlite3.connect('customer.db')
    c= conn.cursor()
    # here email is tuple therefore (email,)
    c.execute("SELECT rowid, * from customers WHERE email= (?)",(email,))
    
    # to see the data fetched
    items=c.fetchall()
    for item in items:
        print(item)
        
    conn.commit()
    conn.close()
