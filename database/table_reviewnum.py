import mysql.connector
import crawling

def create_table(db_name):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database=db_name)
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE numOfReviews (name VARCHAR(255), num TINYINT)')

    sql = 'INSERT INTO numOfReviews (name, num) VALUES (%s, %s)'
    val = []

    for i in range (0, len(crawling.caf_score_list)):
        val_list = []
        num = len(crawling.caf_score_list[i]) - 1
        val_list.append(crawling.caf_score_list[i][0])
        val_list.append(num)
        val.append(tuple(val_list))

    mycursor.executemany(sql, val)
    mydb.commit()

    mydb.close()
