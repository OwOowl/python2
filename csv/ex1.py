import os, re
import usecsv as us

os.chdir(r'C:\Python\crawling\csv\data')
# os.chdir(r'.\data')

total = us.opencsv('popSeoul.csv')
for i in total[:5]:
    print(i)

newPop = us.switch(total)
for i in newPop[:5]:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        print(i[0], foreign)
    except:
        pass

new = [['구', '한국인', '외국인', '외국인 비율(%)']]

for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            new.append([i[0], i[1], i[2], foreign])
    except:
        pass

print(new)
us.writecsv('newPop.csv', new)
