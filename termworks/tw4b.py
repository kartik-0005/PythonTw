# -*- coding: utf-8 -*-
"""
1. Write a Python program to perform the following:
a. Create a database named “products.db”
b. Create a table named “products” that has the following fields:
		prodID: int
        name: text
        quantity: int
        price: real
c. Insert n records into the table reading the values for each item from the user.
d. Display the recordset after fetching all the rows.
e. Delete a product whose product ID is entered by the user.
f. Increase the price of all products whose current price is less than Rs.50, by 10%.
g. Display all the products whose quantity is less than 40.
"""
import sqlite3

from tw4 import ProductsClass

try:
    dbc = ProductsClass("Prod.sqlite")
    conn = sqlite3.connect(dbc.dbName)
    conn.row_factory = sqlite3.Row
    
    
    dbc.dbCreate(conn)
    
    dbc.dbInsert(conn)
    dbc.dbDisplayAll(conn)
    
    dbc.dbDelete(conn)
    
    dbc.dbUpdate(conn)
    dbc.dbDispProd(conn)
    
except:
    print("DBError")
finally:
    conn.close()






