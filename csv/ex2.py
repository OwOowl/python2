import re, os
import usecsv as uc

os.chdir(r'.\data')

apt = uc.switch(uc.opencsv('apt_202210.csv'))

# for i in apt[:6]:
#     print(i[-7])
#
# print('거래개수 : %s' % len(apt))

new_list = []
for i in apt:
    try:
        # 강원도에 크기는 120 이상, 거래금액 3억 이상인 조건
        if i[5] > 120 and i[-7] <= 30000 and re.match('강원', i[0]):
            # print(i[0], i[4], i[-4], i[-7])
            new_list.append([i[0], i[4], i[-4]])
    except:
        pass

print(len(new_list))
uc.writecsv('over120_lower30000.csv', new_list)
