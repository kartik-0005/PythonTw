import sqlite3

def create_table():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                      prodID INTEGER PRIMARY KEY,
                      name TEXT,
                      quantity INTEGER,
                      price REAL
                   )''')
    
    conn.commit()
    conn.close()

def insert_records(n):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    
    for _ in range(n):
        prodID = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        
        cursor.execute("INSERT INTO products (prodID, name, quantity, price) VALUES (?, ?, ?, ?)",
                       (prodID, name, quantity, price))
    
    conn.commit()
    conn.close()

def display_records():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM products")
    records = cursor.fetchall()
    
    for record in records:
        print(record)
    
    conn.close()

def delete_product(prodID):
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM products WHERE prodID = ?", (prodID,))
    
    conn.commit()
    conn.close()

def increase_price():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE products SET price = price * 1.1 WHERE price < 50")
    
    conn.commit()
    conn.close()

def display_low_quantity_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM products WHERE quantity < 40")
    records = cursor.fetchall()
    
    for record in records:
        print(record)
    
    conn.close()

if __name__ == "__main__":
    create_table()
    
    n = int(input("Enter the number of records to insert: "))
    insert_records(n)
    
    print("Records in the table:")
    display_records()
    
    delete_id = int(input("Enter the product ID to delete: "))
    delete_product(delete_id)
    
    increase_price()
    
    print("Products with low quantity:")
    display_low_quantity_products()
