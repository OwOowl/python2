# 교촌치킨 크롤링

import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd


def kyochon_store(result):
    for i in range(1, 18):
        for j in range(1, 100):
            try:
                kyochon_url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%d&sido2=%d' % (i, j)
                print(kyochon_url)
                html = urllib.request.urlopen(kyochon_url)
                kyochonSoup = bs(html, 'html.parser')
                tag_ul = kyochonSoup.find('ul', attrs={'class': 'list'})
                for store_data in tag_ul.findAll('a'):
                    store_name = store_data.find('strong').get_text()
                    store_address = store_data.find('em').get_text().strip().split('\r')[0]
                    store_sido_gu = store_address.split()[:2]
                    result.append([store_name] + store_sido_gu + [store_address])
            except:
                if j >= 25:
                    break
                else:
                    pass


def main():
    result = []
    kyochon_store(result)
    kyochon_tbl = pd.DataFrame(result, columns=('store', 'si', 'do', 'address'))
    kyochon_tbl.to_csv('./data/kyochon_store.csv', encoding='cp949', mode='w', index=True)
    print('완료~~')
    del result[:]


if __name__ == '__main__':
    main()
