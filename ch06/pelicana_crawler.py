# 페리카나 크롤링

import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd


def pelicana_store(result):
    for page in range(1, 108):
        pelicana_url = 'https://pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si=' % page
        html = urllib.request.urlopen(pelicana_url)
        pelicanaSoup = bs(html, 'html.parser')
        tag_tbody = pelicanaSoup.find('tbody')
        for store in tag_tbody.find_all('tr'):
            store_td = store.find_all_next('td')
            store_name = store_td[0].string
            store_address = store_td[1].string
            store_phone = store_td[2].string
            result.append([store_name] + [store_address] + [store_phone])


def main():
    result = []
    pelicana_store(result)
    pelicana_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    pelicana_tbl.to_csv('./data/pelicana_store.csv', encoding='cp949', mode='w', index=True)
    print('완료~~~')
    del result[:]


if __name__ == '__main__':
    main()
