import re, os
import usecsv as uc

os.chdir(r'.\data')
apt = uc.switch(uc.opencsv('apt_202210.csv'))

newList = []
for i in apt:
    try:
        if (i[5] >= 150 or i[-7] >= 50000) and re.match('부산', i[0]):
            # print(i[0], i[4], i[-4], i[-7])
            newList.append([i[0], i[4], i[-4]])
    except:
        pass

print(len(newList))
uc.writecsv('over150+high50000.csv', newList)
