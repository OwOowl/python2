# 할리스 매장 크롤링

import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd


def hollys_store(result):
    for page in range(1, 54):   # p.173 와 페이지수가 달라졌기에 확인요소
        hollys_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' % page
        # print(hollys_url)
        html = urllib.request.urlopen(hollys_url)
        soupHollys = bs(html, 'html.parser')
        tag_body = soupHollys.find('tbody')
        # print(tag_body)
        for store in tag_body.find_all('tr'):
            store_td = store.find_all_next('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            # print('%s %s %s %s' % (store_name, store_sido, store_address, store_phone))
            result.append([store_name] + [store_sido] + [store_address] + [store_phone])


def main():
    result = []
    hollys_store(result)
    hollys_tbl = pd.DataFrame(result, columns=('store', 'sido_gu', 'address', 'phone'))
    hollys_tbl.to_csv('./data/hollys.csv', encoding='cp949', mode='w', index=True)
    print('완료~~')
    del result[:]


if __name__ == '__main__':
    main()


