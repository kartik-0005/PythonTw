
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

from contextlib import closing

class ProductsClass:
    def __init__(self,dbName):
        self.dbName = dbName
        
    
    def dbCreate(self,conn):
        cursorObj = conn.cursor()
        cursorObj.execute('Create table if not exists Products(prodId INTEGER, name TEXT, qty INTEGER, price INTEGER, PRIMARY KEY(prodID))')
        conn.commit()
        
    def dbInsert(self, conn): 
        n = int(input("Enter no. of records:"))
        for i in range(n):
            prodID = int(input("Enter prodID"))
            name = input("Enter name:")
            qty = int(input("Enter quantity:"))
            price = int(input("Enter price"))
            entities = (prodID, name, qty, price)
            cursorObj = conn.cursor()
            cursorObj.execute('Insert into Products(prodID,name,qty,price) values (?,?,?,?)',entities)
        conn.commit()
        
    def dbDisplayAll(self,conn):
        cursorObj = conn.cursor()
        cursorObj.execute('Select * from Products')
        rs = cursorObj.fetchall()
        for row in rs:
            row = list(row)
            print(row)       #printall. Here only the 1st field is printed
               
    def dbDelete(self,conn):
        prodID = int(input("Enter the prodID "))
        cursorObj = conn.cursor()
        sqlStr = "delete from Products where prodID = ?"
        cursorObj.execute(sqlStr, (prodID,))
        conn.commit()
    
    
    def dbUpdate(self,conn):
        cursorObj = conn.cursor()
        cursorObj.execute('Update Products SET price = price+price * 0.1 where price < 50')
        conn.commit()
    
    def dbDispProd(self,conn):
        cursorObj = conn.cursor()
        cursorObj.execute('Select name from Products where qty < 40')
        rs = cursorObj.fetchall()
        for row in rs:
            print(row[0])       
               
