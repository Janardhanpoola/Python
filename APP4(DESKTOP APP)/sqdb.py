import sqlite3

def create_table():
    #1.connect to db
    conn=sqlite3.connect("lite.db")

    #2.create cursor
    cur=conn.cursor()

    #3.execute sql stmnt
    cur.execute("CREATE TABLE if not exists store (item TEXT,quantity INTEGER,price REAL)")

    #4.commit the changes
    conn.commit()

    #5.close the connection
    conn.close()


def insert_table(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

#insert_table("chair",2,83)
#insert_table("tables",5,1500)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? where item=?",(quantity,price,item))
    conn.commit()
    conn.close()


update(5,183,"chair")
#delete("tables")


print(view())

