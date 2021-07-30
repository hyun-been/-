import mysql.connector

def print_review(restaurant):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT name, review FROM reviews WHERE name =' + restaurant)
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수
    while True:
        print(row)
