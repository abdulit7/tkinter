import sqlite3

def create_db():

    conn = sqlite3.connect(database=r'store.db')
    cursor = conn.cursor()
    cursor.execute("create table if not exists employee(eid integer primary key autoincrement,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    conn.commit()

    cursor.execute("create table if not exists supplier(invoice integer primary key autoincrement,name text,contact text,desc text)")
    conn.commit()

    cursor.execute("create table if not exists category(cid integer primary key autoincrement,name text)")
    conn.commit()

    cursor.execute("create table if not exists product(pid integer primary key autoincrement,Category text,Supplier text,Name text,Price text,QTY text,Status text)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS sales(invoice_id INTEGER PRIMARY KEY,customer_name TEXT NOT NULL,contact TEXT NOT NULL,product_name TEXT NOT NULL,quantity INTEGER NOT NULL,price REAL NOT NULL,total REAL NOT NULL,date TEXT NOT NULL)")
    conn.commit()
    
create_db()


