import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cursor=self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS BOOKS1 (SERIALID INTEGER PRIMARY KEY,TITLE TEXT,AUTHOR TEXT,year integer,ISBN INTEGER) ")
        self.conn.commit()



    def insert(self,title,author,year,isbn):
        self.cursor.execute("INSERT INTO BOOKS1 VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def viewall(self):
        self.cursor.execute("select * from books1")
        rows=self.cursor.fetchall()
        return rows
    

    def search(self,title="",author="",year="",isbn=""):
        self.cursor.execute("select * from books1 where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
        rows=self.cursor.fetchall()
        return rows    

    def update(self,title,author,year,isbn,serialid):
        self.cursor.execute("UPDATE BOOKS1 SET TITLE=?,AUTHOR=?,YEAR=?, ISBN=? WHERE SERIALID=?",(title,author,year,isbn,serialid))
        self.conn.commit()

    def delete(self,serialid):
        self.cursor.execute("DELETE FROM BOOKS1 WHERE SERIALID=?",(serialid,))
        self.conn.commit()
    def __del__(self):
        self.conn.close()


#delete(7)
#connect()
#insert("THE SUN","JOHN",1975,876)
#update('The MOON',"Henry T",1947,"783773",4)
#print(viewall())
#print(search(author="rock"))