from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen('https://www.kyobobook.co.kr/bestSellerNew/bestseller.laf')

soup = bs(html.read(), 'html.parser')

book_page_urls = []

for i in soup.find_all('div', {'class': 'sub_title_wrap'}):
    print(i.text)

