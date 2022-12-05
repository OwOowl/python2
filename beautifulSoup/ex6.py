import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

article1 = 'https://n.news.naver.com/mnews/article/015/0004783532?sid=105'
html = ur.urlopen(article1)
soup = bs(html.read(), 'html.parser')

f = open('./data/links2.txt', 'w', encoding='utf-8')

# 헤드라인 출력
headLine = soup.find_all('h2', {'id': 'title_area'})[0].text
print(headLine)
headLine = soup.find_all('h2', class_='media_end_head_headline')[0].text
print(headLine)

# 특정 기사 본문 저장하기
for i in soup.find_all('div', {'class': 'go_trans _article_content'}):
    f.write(i.text + '\n')
f.close()
print('End~~~')
