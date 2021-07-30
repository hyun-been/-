import mysql.connector
import crawling

def create_table(db_name):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database=db_name)
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE scores (name VARCHAR(255), score FLOAT)')

    sql = 'INSERT INTO scores (name, score) VALUES (%s, %s)'
    val = []

    for i in range (0, len(crawling.caf_score_list)):
        score = 0
        for j in range(1, len(crawling.caf_score_list[i])):
            score += int(float(crawling.caf_score_list[i][j]))
##        print(score, end =' ')
##        print(len(crawling.caf_score_list[i]) - 1)
        val_list = []
        avg_score = score / (len(crawling.caf_score_list[i]) - 1)
        val_list.append(crawling.caf_score_list[i][0])
        val_list.append(round(avg_score, 1)) ## 소수점 첫째자리까지 표현
        val.append(tuple(val_list))

    mycursor.executemany(sql, val)
    mydb.commit()

    mydb.close()
