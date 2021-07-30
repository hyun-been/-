from selenium import webdriver
from selenium.webdriver.common.keys import Keys ## 로그인 버튼 클릭
from bs4 import BeautifulSoup
from konlpy.tag import Kkma ## 명사만 추출
import mysql.connector
import time ## sleep
import sys
import io
import crawling
import create_database
import delete_database
import table_review
import table_classify
import table_score
import table_reviewnum
import table_address
import review_insert

## main 함수
def main():
    chromedriver = 'C:\WebDriver\chromedriver.exe'  ## chromedriver.exe가 저장된 경로(path)
    browser = webdriver.Chrome(chromedriver)
    browser.implicitly_wait(1)

    browser.get('https://everytime.kr/login')
    ## ID = input('사용자의 아이디를 입력하세요: ')
    ## passwd = input('사용자의 비밀번호를 입력하세요: ')

    browser.find_element_by_name('userid').send_keys('아이디')
    browser.find_element_by_name('password').send_keys('비밀번호')
    browser.find_element_by_tag_name('input').send_keys(Keys.RETURN)
    time.sleep(1)

    pages = [4, 7, 16, 48, 94]

    for i in range(0, 5):
        page = 1
        n = 0
        while n < pages[i]:
            crawling.next_page(browser, i+1, page)

            res = browser.page_source
            html = BeautifulSoup(res, "html.parser")

            crawling.posts_crawling(html, crawling.post_list)
            crawling.url_crawling(html, crawling.post_url_list)

            page += 1
            n += 1

    crawling.remove_posts(crawling.post_list, crawling.post_url_list)
    crawling.arrange_post(crawling.post_list)
    crawling.get_caf_list(crawling.post_list, crawling.caf_list)

    crawling.get_review_list(crawling.post_list, crawling.caf_list, crawling.caf_post_list)
    crawling.get_url_list(crawling.post_list, crawling.post_url_list, crawling.caf_list, crawling.caf_url_list)
    crawling.get_score_list(crawling.caf_post_list, crawling.caf_score_list)

    crawling.arrange_lists(crawling.caf_list, crawling.caf_post_list, crawling.caf_url_list, crawling.caf_score_list)
    crawling.slice_review(crawling.caf_post_list)
    crawling.remove_empty_list(crawling.caf_post_list, crawling.caf_url_list, crawling.caf_score_list)

    crawling.arrange_caf(crawling.caf_list, crawling.caf_post_list, crawling.caf_url_list, crawling.caf_score_list)

##    for i in range(0, len(crawling.caf_post_list)):
##        for post in crawling.caf_post_list[i]:
##            print(post)

##    for j in range(0, len(crawling.caf_url_list)):
##        for address in crawling.caf_url_list[j]:
##            print(address)

##    for k in range(0, len(crawling.caf_score_list)):
##        for score in crawling.caf_score_list[k]:
##            print(score, end = ' ')
##        print()

##    print(len(crawling.caf_list))
##    print(len(crawling.caf_post_list))
##    print(len(crawling.caf_url_list))
##    print(len(crawling.caf_score_list))

    browser.quit() ## 창 종료

    ## 수집한 데이터를 mysql로 데이터베이스에 저장
    try:
        create_database.create_db()
    except:
        delete_database.delete_db()
        create_database.create_db()

    ## 식당을 중식/양식/한식/분식 등으로 구분한 데이터베이스로 저장
    table_classify.create_table('Cafeteria_schema')

    ## 식당에 대한 평균 점수를 데이터베이스로 저장
    table_score.create_table('Cafeteria_schema')

    ## 식당의 리뷰 수 저장
    table_reviewnum.create_table('Cafeteria_schema')

    ## 식당 주소, 전화번호 데이터베이스에 저장
    table_address.create_table('Cafeteria_schema')

    ## 리뷰 데이터베이스에 저장
    table_review.create_table('Cafeteria_schema')
    review_insert.fill_db('Cafeteria_schema')

## main 실행
if __name__ == "__main__":
    main()
