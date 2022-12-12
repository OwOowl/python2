# 교촌치킨 크롤링

import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd


def kyochon_store(result):
    for i in range(1, 18):
        for j in range(1, 45):
            try:
                kyochon_url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%d&sido2=%d' % (i, j)
                print(kyochon_url)
                html = urllib.request.urlopen(kyochon_url)
                kyochonSoup = bs(html, 'html.parser')

            except:
                continue
    return



def main():
    result = []
    kyochon_store(result)
    kyochon_tbl = pd.DataFrame(result, columns=('store', 'address'))
    kyochon_tbl.to_csv('./data/kyochon_store.csv', encoding='cp949', mode='w', index=True)
    print('완료~~')
    del result[:]


if __name__ == '__main__':
    main()