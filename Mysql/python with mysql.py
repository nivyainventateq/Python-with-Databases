import mysql.connector as mysql

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connect(host="localhost",user='root',password='Nivya@123', database='sampledata')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Cannot connect to database")

    def create_databse(self):
        try:
            x="create database userdb"
            self.cursor.execute(x)
            print("database created")
        except:
            self.cursor.execute('show databases')
            for i in self.cursor:
                print(i)

    def create_table(self):
        try:
            create_table_command = "CREATE TABLE IF NOT EXISTS Student(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
            self.cursor.execute(create_table_command)
            print("table created")
            self.cursor.execute('show tables')
            for i in self.cursor:
                print(i)
        except:
            import sys
            print(sys.exc_info())

    def insert_new_record(self):
        insert_command="INSERT INTO Employee(name,age) VALUES ('Alice',27)"
        # insert_command = "INSERT INTO Employee(name, age) VALUES('sunil','76')"
        print(insert_command)
        self.cursor.execute(insert_command)

    def query_all(self):
        self.cursor.execute("SELECT * FROM Employee ")
        X = self.cursor.fetchall()
        for i in X:
            print(i)

    def update_record(self):
        update_command = "UPDATE Employee SET age=10 WHERE id=1"
        self.cursor.execute(update_command)
        print(update_command)


    def drop_table(self):
        drop_table_command = "DROP TABLE pet"
        self.cursor.execute(drop_table_command),print("deleted sucessfully")

if __name__== '__main__':
    database_connection = DatabaseConnection()
    database_connection.create_databse()
    # database_connection.create_table()
    # database_connection.insert_new_record()
    # database_connection.query_all()
    # database_connection.update_record()
    # database_connection.drop_table()












