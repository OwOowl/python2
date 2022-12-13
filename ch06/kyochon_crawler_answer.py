# 교촌 매장 정보 크롤링 해설

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


def getKyochonAddress(sido1, result):
    for sido2 in count():
        url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (str(sido1), str(sido2 + 1))
        try:
            rcv_data = get_request_url(url)
            soupData = BeautifulSoup(rcv_data, 'html.parser')
            ul_tag = soupData.find('ul', attrs={'class': 'list'})
            for store_data in ul_tag.findAll('a', href=True):
                store_name = store_data.find('strong').get_text()
                store_address = store_data.find('em').get_text().strip().split('\r')[0]
                store_sido_gu = store_address.split()[0:2]
                result.append([store_name] + store_sido_gu + [store_address])
        except:
            break
    return


def cswin_Kyochon():
    result = []
    print('Kyochon Address Crawling Start')
    for sido1 in range(1, 18):
        getKyochonAddress(sido1, result)
    Kyochon_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    Kyochon_table.to_csv('./data/kyochon.csv', encoding='cp949', mode='w', index=True)
    del result[:]
    print('FINISH')


if __name__ == '__main__':
    cswin_Kyochon()



