import mysql.connector

def print_score_kor():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "한식" ORDER BY num DESC') ## 리뷰 수 순으로 한식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_score_wes():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "양식" ORDER BY num DESC') ## 리뷰 수 순으로 양식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_score_jap():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "일식" ORDER BY num DESC') ## 리뷰 수 순으로 일식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_score_chin():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "중식" ORDER BY num DESC') ## 리뷰 수 순으로 중식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_score_flour():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "분식" ORDER BY num DESC') ## 리뷰 수 순으로 분식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_score_fast():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "패스트푸드" ORDER BY num DESC') ## 리뷰 수 순으로 패스트푸드점 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_score_caf():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "카페" OR restaurants.kind = "디저트" ORDER BY num DESC') ## 리뷰 수 순으로 카페 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_score_etc():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "기타" ORDER BY num DESC') ## 리뷰 수 순으로 기타 식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_score_total():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, score FROM numOfReviews JOIN scores ON numOfReviews.name = scores.name ORDER BY num DESC') ## 리뷰 수 순으로 식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수


def print_address_kor():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name  JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "한식" ORDER BY num DESC') ## 리뷰 수 순으로 한식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_address_wes():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name  JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "양식" ORDER BY num DESC') ## 리뷰 수 순으로 양식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_address_jap():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name  JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "일식" ORDER BY num DESC') ## 리뷰 수 순으로 일식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_address_chin():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name  JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "중식" ORDER BY num DESC') ## 리뷰 수 순으로 중식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_address_flour():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name  JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "분식" ORDER BY num DESC') ## 리뷰 수 순으로 분식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_address_fast():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name  JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "패스트푸드" ORDER BY num DESC')
    ## 리뷰 수 순으로 패스트푸드점 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_address_caf():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name  JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "카페" or restaurants.kind = "디저트" ORDER BY num DESC') ## 리뷰 수 순으로 카페 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_address_etc():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name  JOIN restaurants ON numOfReviews.name = restaurants.name WHERE restaurants.kind = "기타" ORDER BY num DESC') ## 리뷰 수 순으로 기타 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수

def print_address_total():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database='Cafeteria_schema')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT numOfReviews.name, address.address, number FROM numOfReviews JOIN address ON numOfReviews.name = address.name ORDER BY num DESC') ## 리뷰 수 순으로 전체 식당 정렬
    row = mycursor.fetchone() ## 한 줄 단위로 저장하는 함수
