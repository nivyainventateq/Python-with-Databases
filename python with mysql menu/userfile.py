import mysql.connector as connector

class SampleDatabase:

    def __init__(self):
        self.connection = connector.connect(host="localhost", user='root', password='Nivya@123', database='pythontest')
        query='create table if not exists user(userid serial PRIMARY KEY, username varchar(20), phone varchar(10))'
        cur=self.connection.cursor()
        cur.execute(query)
        print("table created")

    # Insert
    def insert(self,userid,username,phone):
        query="insert into user (userid,username,phone) values({}, '{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        print("user data saved to database")

    #fetch/retrive

    def fetch(self):
        query='select * from user'
        cur=self.connection.cursor()
        cur.execute(query)
        for row in cur:
            print('userid:',row[0])
            print('username:',row[1])
            print('phone:',row[2])
            print()

    # delete the record from table

    def delete(self,userid):
        query='delete from user where userid={}'.format(userid)
        print(query)
        cur=self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        print("record deleted")

    # update the record from table

    def update(self, userid,newname,newphone):
        query ="update user set username='{}',phone='{}' where userid={}".format(newname,newphone,userid)
        print(query)
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        print("record updated")

db=SampleDatabase()
# db.insert(11,"nivya",8638638)
# db.insert(12,"Santhu",279378)
# db.insert(13,"Amar",7384864)
# db.insert(14,"Kavya",3828372)
# db.fetch()
# db.delete(11)
# db.fetch()
# db.update(14,"Ram",92974)
db.fetch()
