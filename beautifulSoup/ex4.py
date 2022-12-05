from urllib.request import urlopen as ur
from bs4 import BeautifulSoup as bs

url = 'http://news.daum.net/'

html = ur(url)
soup = bs(html.read(), 'html.parser')

# item_issue = soup.find_all('div', {'class': 'item_issue'})
# for issue in item_issue:
#     print(issue.text)

# print(soup.find_all('a')[:5])

# for i in soup.find_all('a'[0:10]):
#     print(i.get('href'))

# for i in soup.find_all('div', class_='item_issue'):
#     print(i.find_all_next('a'))

for i in soup.find_all('div', {'class': 'item_issue'}):
    # ah = i.find_all('a')[0].get('href')
    # print(ah)
    soup2 = bs(ur(i.find_all('a')[0].get('href')).read(), 'html.parser')
    print(soup2)

