import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        qry='''
         create table if not exists employee(
         id integer primary key,
         name text,
         age text,
         city text,
         gender text,
         mail text,
         contact text,
         address text
         ) 
        '''
        self.cur.execute(qry)
        self.con.commit()

    def insert(self,name,age,city,gender,mail,contact,address):
        self.cur.execute("insert into employee values(null,?,?,?,?,?,?,?)",(name,age,city,gender,mail,contact,address))
        self.con.commit()

    def update(self,name,age,city,gender,mail,contact,address,id):
        self.cur.execute("update employee set name=?,age=?,city=?,gender=?,mail=?,contact=?,address=? where id=?",(name,age,city,gender,mail,contact,address,id))
        self.con.commit()

    def delete(self,id):
        self.cur.execute("delete from employee where id=?",(id,))
        self.con.commit()

    def select(self):
        self.cur.execute("select * from employee")
        rows=self.cur.fetchall()
        #print(rows)
        return rows



