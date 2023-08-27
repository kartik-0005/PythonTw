import sqlite3
from contextlib import closing

    

def insertDB(conn):
    n=int(input("Enter the number of entries you want to make"))
    while n!=0:
        id=int(input("Enter product id"))
        name=input("Enter product name")
        qty=int(input("Enter quantity"))
        price=input("Enter price")
        cursorobj=conn.cursor()
        cursorobj.execute('Insert into Students(prodID,name,quantity,price) values(?,?,?,?)',(id,name,qty,price))
        n=n-1
    conn.commit()
    conn.close()
        

def displayDB(self,conn):
    pass

def delete(self,conn):
    pass

def update(self,conn):
    pass

def main():
    conn=sqlite3.connect("school.db")
    cursorObj=conn.cursor()
    cursorObj.execute('Create table if not exists Products(prodID integer,name varchar(20),quantity intger,price real)')
    conn.commit
    insertDB(conn)

if __name__ =="__main__":
    main()
    
