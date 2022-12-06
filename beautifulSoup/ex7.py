import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://news.daum.net/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')

f = open('./data/article_total.txt', 'w', encoding='utf-8')

for i in soup.find_all('div', {'class': 'item_issue'}):
    try:
        # print(i.text)
        # print(i.text)
        f.write(i.text + '\n')
        f.write(i.find_all('a')[0].get('href') + '\n')
        html2 = ur.urlopen(i.find_all('a')[0].get('href'))
        soup2 = bs(html2.read(), 'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text + '\n')
    except:
        pass
f.close()


