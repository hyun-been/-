from selenium import webdriver
from selenium.webdriver.common.keys import Keys ## 로그인 버튼 클릭
from bs4 import BeautifulSoup
from konlpy.tag import Kkma ## 명사만 추출
import time ## sleep
import sys
import io
import remove_emoji

## 전역 변수 설정
post_list = []
post_url_list = []
caf_list = []

caf_post_list = []
caf_url_list = []
caf_score_list = []

## 유니코드 변환
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

## 벗들의 맛집 게시판에서 게시글 추출하는 함수
def posts_crawling(html, post_list):
    posts = html.select('#container > div.wrap.articles > article > a > p')
    for post in posts:
        post_list.append(post.text) ## 게시글 내용을 배열에 저장

## 벗들의 맛집 게시판에서 들고온 게시글의 url 주소 저장
def url_crawling(html, post_url_list):
    posts = html.select('#container > div.wrap.articles > article > a')
    for post in posts:
        post_url_list.append('https://ewha.everytime.kr' + post.attrs['href']) ## 게시물 url을 배열에 저장

## 게시판 페이지 넘기는 함수
def next_page(browser, score, page):
    browser.get('https://ewha.everytime.kr/260176/hashtag/' + str(score) + '/p/' + str(page))
    time.sleep(1)

## 타지역 게시글들을 list에서 삭제하는 함수
def remove_posts(post_list, post_url_list):
    remove_list = ['타지역', '타지역주의', '연남동', '홍대', '신촌', '배달', '스마트', '스토어', '망원', '합정', '청담']
    remove_list_index = []
    for i in range (0, len(post_list)):
        kkma = Kkma()
        post_nouns_list = kkma.nouns(post_list[i]) ## 추출한 게시물들을 명사 단위로 쪼개기
        post_nouns_list = post_nouns_list[0:10] ## 10개만 추출
        for noun in post_nouns_list:
            if noun in remove_list: ## 추출한 명사가 삭제할 게시글에 포함된 명사를 포함할 때
                remove_list_index.append(i)
                break
    for index in remove_list_index:
        post_list[index] = 'null'
        post_url_list[index] = 'null'
    for j in range(0, len(remove_list_index)):
        post_list.remove('null')
        post_url_list.remove('null')

## 게시글에서 식당 이름을 추출하는 함수
def get_caf_list(post_list, caf_list):
    for i in range(0, len(post_list)):
        post_separate_list = post_list[i].split('/')
        if (len(post_separate_list[0]) < 7) and (len(post_separate_list[0]) > 1): ## 양식을 지키지 않은 게시글에서 식당을 추출할 수 없음
            if (post_separate_list[0] != ' ') and (post_separate_list[0] != '25') and (post_separate_list[0] != '.'):
                if post_separate_list[0] not in caf_list: ## caf_list에 중복되지 않게 식당 저장
                    caf_list.append(post_separate_list[0])
    caf_list = caf_list.sort()

## 식당 이름에 따라 리뷰를 저장하는 함수
def get_review_list(post_list, caf_list, caf_post_list):
    for i in range(0, len(caf_list)):
        caf_post_list.append([])
        caf_post_list[i].append(caf_list[i])
    for j in range(0, len(post_list)):
        post_separate_list = post_list[j].split('/')
        for k in range(0, len(caf_list)):
            if post_separate_list[0] == caf_list[k]:
                caf_post_list[k].append(post_list[j])

## 식당 이름에 따라 url을 저장하는 함수
def get_url_list(post_list, post_url_list, caf_list, caf_url_list):
    for i in range(0, len(caf_list)):
        caf_url_list.append([])
        caf_url_list[i].append(caf_list[i])
    for j in range(0, len(post_list)):
        post_separate_list = post_list[j].split('/')
        for k in range(0, len(caf_list)):
            if post_separate_list[0] == caf_list[k]:
                caf_url_list[k].append(post_url_list[j])

## 점수를 2차원 배열에 저장하는 함수
def get_score_list(caf_post_list, caf_score_list):
    for i in range(0, len(caf_post_list)):
        caf_score_list.append([])
        caf_score_list[i].append(caf_post_list[i][0]) ## 식당 이름 저
        for j in range(1, len(caf_post_list[i])):
            post_separate_list = list(caf_post_list[i][j])
            for k in range(0, len(post_separate_list)):
                if post_separate_list[k] == '#': ## 게시글 내용 중 #의 인덱스를 찾아서 다음 글자인 점수를 추출
                    caf_score_list[i].append(post_separate_list[k+1])
                    break

    #for i in range(0, len(caf_list)):
    #    caf_score_list.append([])
    #    caf_score_list[i].append(caf_list[i])
    #for j in range(0, len(post_list)):
    #    post_separate_list = post_list[j].split('/')
    #    letter_separate_list = list(post_list[j])
    #    for k in range(0, len(caf_list)):
    #        if post_separate_list[0] == caf_list[k]:
    #            index = 0
    #            for l in range(0, len(letter_separate_list)): ## 게시글 내용 중 #의 인덱스를 찾아서 다음 글자인 점수를 추출
    #               if letter_separate_list[l] == '#':
    #                    index = l
    #                    break
    #            caf_score_list[k].append(letter_separate_list[l+1])

## 식당목록에서 띄어쓰기 삭제 후 동일한 식당을 하나의 list로 생략
def arrange_lists(caf_list, caf_post_list, caf_url_list, caf_score_list):
    for i in range(0, len(caf_post_list)):
        separate_caf_word = list(caf_list[i])
        separate_post_word = list(caf_post_list[i][0])
        separate_url_word = list(caf_url_list[i][0])
        separate_score_word = list(caf_score_list[i][0])
        count = 0
        for letter in separate_post_word:
            if letter == ' ':
                count += 1
        for k in range(0, count):
            separate_caf_word.remove(' ')
            separate_post_word.remove(' ')
            separate_url_word.remove(' ')
            separate_score_word.remove(' ')
        try:
            caf_list[i] = separate_caf_word[0]
            caf_post_list[i][0] = separate_post_word[0]
            caf_url_list[i][0] = separate_url_word[0]
            caf_score_list[i][0] = separate_score_word[0]
        except:
            pass
        for j in range(1, len(separate_post_word)):
            caf_list[i] += separate_caf_word[j]
            caf_post_list[i][0] += separate_post_word[j]
            caf_url_list[i][0] += separate_url_word[j]
            caf_score_list[i][0] += separate_score_word[j]
    for k in range(0, len(caf_post_list)):
        for l in range(k+1, len(caf_post_list)):
            if caf_post_list[k][0] == caf_post_list[l][0]:
                caf_list[l] = 'null'
                caf_post_list[k] = caf_post_list[k] + caf_post_list[l][1:]
                caf_url_list[k] = caf_url_list[k] + caf_url_list[l][1:]
                caf_score_list[k] = caf_score_list[k] + caf_score_list[l][1:]
                for m in range(0, len(caf_post_list[l])):
                    caf_post_list[l][m] = 'null'
                    caf_url_list[l][m] = 'null'
                    caf_score_list[l][m] = 'null'
    try:
        while True:
            caf_list.remove('null')
    except:
        pass
    for n in range(0, len(caf_post_list)):
        try:
            while True:
                caf_post_list[n].remove('null')
                caf_url_list[n].remove('null')
                caf_score_list[n].remove('null')
        except:
            pass

## 게시글의 길이를 50자로 제한하고 게시글 뒤에 더보기 추가
def slice_review(caf_post_list):
    for i in range(0, len(caf_post_list)):
        for j in range(1, len(caf_post_list[i])):
            separate_post_list = list(caf_post_list[i][j])
            if len(separate_post_list) > 50:
                separate_post_list = separate_post_list[0:50]
                caf_post_list[i][j] = separate_post_list[0]
                for k in range(1, len(separate_post_list)):
                    caf_post_list[i][j] += separate_post_list[k]
            caf_post_list[i][j] += ' ... 더보기'

## 의미없이 존재하는 빈 list 삭제
def remove_empty_list(caf_post_list, caf_url_list, caf_score_list):
    try:
        while True:
            caf_post_list.remove([])
            caf_url_list.remove([])
            caf_score_list.remove([])
    except:
        pass

## 게시글에서 이모지 제거
def arrange_post(post_list):
    for i in range(0, len(post_list)):
        post_list[i] = remove_emoji.demoji(post_list[i])

## 식당 이름 통일하기
def arrange_caf(caf_list, caf_post_list, caf_url_list, caf_score_list):
    for i in range (0, len(caf_list)):
        caf_post_list[i][0] = caf_list[i]
        caf_url_list[i][0] = caf_list[i]
        caf_score_list[i][0] = caf_list[i]
