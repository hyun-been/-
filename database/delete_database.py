import mysql.connector

def delete_db():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf')
    mycursor = mydb.cursor()
    mycursor.execute('DROP DATABASE Cafeteria_schema')
    mydb.close()
