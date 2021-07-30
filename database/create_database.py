import mysql.connector

def create_db():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf')
    mycursor = mydb.cursor()
    mycursor.execute('CREATE DATABASE Cafeteria_schema')
    mydb.close()
