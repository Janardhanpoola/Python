import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS BOOKS1 (SERIALID INTEGER PRIMARY KEY,TITLE TEXT,AUTHOR TEXT,year integer,ISBN INTEGER) ")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO BOOKS1 VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()    

def viewall():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books1")
    rows=cursor.fetchall()
    conn.close()
    return rows
  

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books1 where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows=cursor.fetchall()
    conn.close()
    return rows    

def update(title,author,year,isbn,serialid):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE BOOKS1 SET TITLE=?,AUTHOR=?,YEAR=?, ISBN=? WHERE SERIALID=?",(title,author,year,isbn,serialid))
    conn.commit()
    conn.close()

def delete(serialid):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM BOOKS1 WHERE SERIALID=?",(serialid,))
    conn.commit()
    conn.close()


#delete(7)
#connect()
#insert("THE SUN","JOHN",1975,876)
#update('The MOON',"Henry T",1947,"783773",4)
#print(viewall())
#print(search(author="rock"))