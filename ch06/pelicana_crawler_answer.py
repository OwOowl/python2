# 페리카나 매장 정보 크롤링 해설
import time
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count

import ssl # 접속 보안 허용


def get_request_url(url, enc='utf-8'):
    req = urllib.request.Request(url)
    try:
        # [SSL: CERTIFICATE_VERIFY_FAILED] 에러 뜰때
        ssl._create_default_https_context = ssl._create_unverified_context  # 접속보안 허용
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                # 한글로 변환
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                # replace : 에러 발생 시 ?로 변환
                ret = rcv.decode(enc, 'replace')
            return ret
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s' % (datetime.datetime.now(), url))
        return None


def getPelicanaAddress(result):
    for page_idx in count():
        url = 'http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=&page=%s' % str(page_idx + 1)
        print('[Pelicana Page] : [%s]' % str(page_idx + 1))
        rcv_data = get_request_url(url)
        soupData = BeautifulSoup(rcv_data, 'html.parser')
        store_table = soupData.find('table', attrs={'class': 'table mt20'})
        tbody = store_table.find('tbody')
        bEnd = True

        for store_tr in tbody.findAll('tr'):
            bEnd = False
            tr_tag = list(store_tr.strings)
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_sido_gu = store_address.split()[0:2]
            result.append([store_name] + store_sido_gu + [store_address])
        if (bEnd == True):
            print(result[0])
            print('==데이터 수 : %d' % len(result))
            return
    return


def cswin_Pelicana():
    result = []
    print('Pelicana Address Crawling Start')
    getPelicanaAddress(result)
    Pelicana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    Pelicana_table.to_csv('./data/pelicana.csv', encoding='cp949', mode='w', index=True)
    del result[:]
    print('FINISH')


if __name__ == '__main__':
    cswin_Pelicana()
