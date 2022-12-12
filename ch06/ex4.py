# 커피빈 매장찾기(동적 웹크롤링)

from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import datetime, time
from selenium import webdriver


# [CODE 1]
def coffeBean_store(result):
   coffeBean_URL = 'https://www.coffeebeankorea.com/store/store.asp'
   wd = webdriver.Chrome('./webdriver/chromedriver.exe')

   for i in range(1, 370):  # 233 -> 234 매장 수 만큼 반복
       wd.get(coffeBean_URL)
       time.sleep(1)    # 웹페이지 연결할 동안 1초 대기
       try:
           wd.execute_script('storePop2(%d)' % i)
           time.sleep(1)    # 스크립트 실행 동안 1초 대기
           html = wd.page_source
           soupCB = bs(html, 'html.parser')

           store_name_h2 = soupCB.select('div.store_txt > h2')
           store_name = store_name_h2[0].string
           store_info = soupCB.select('div.store_txt > table.store_table > tbody > tr > td')
           store_address_list = list(store_info[2])
           store_address = store_address_list[0]
           store_phone = store_info[3].string
           result.append([store_name] + [store_address] + [store_phone])
       except:
           continue
   return


# [CODE 2]
def main():
    result = []
    print('CoffeeBean store crawling~~~~~~~~')
    coffeBean_store(result)
    cb_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    cb_tbl.to_csv('./data/CoffeeBean.csv', encoding='cp949', mode='w', index=True)
    print('완료~~~~')


if __name__ == '__main__':
    main()


