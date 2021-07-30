import mysql.connector
import crawling

def fill_db(db_name):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database=db_name)
    mycursor = mydb.cursor()
    mycursor.execute('ALTER TABLE reviews CHARACTER SET = utf8mb4, COLLATE utf8mb4_unicode_ci')
    sql = 'INSERT INTO reviews (name, review, url, score) VALUES (%s, %s, %s, %s)'
    val = []

    for i in range (0, len(crawling.caf_post_list)):
        for j in range(1, len(crawling.caf_post_list[i])):
            try:
                val_list = []
                val_list.append(crawling.caf_post_list[i][0])
                val_list.append(crawling.caf_post_list[i][j])
                val_list.append(crawling.caf_url_list[i][j])
                val_list.append(crawling.caf_score_list[i][j])
                val.append(tuple(val_list))
##                print(val_list)
            except:
                pass

    mycursor.executemany(sql, val)
    mydb.commit()

    mydb.close()
