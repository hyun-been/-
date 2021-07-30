import mysql.connector

def create_table(db_name):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database=db_name)
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE reviews (name VARCHAR(255), review TEXT, url VARCHAR(255), score TINYINT)')
    mydb.close()
