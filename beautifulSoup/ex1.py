from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.naver.com')

obj = BeautifulSoup(html, 'html.parser')


# for meta in obj.head.find_all('meta'):
#     print(meta.get('content'))

# print(obj.head.find('meta', {'name': 'description'}).get('content'))

for link in obj.find_all('a'):
    print(link.text.strip(), link.get('href'))

