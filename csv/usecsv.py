import csv, re, os


# 파일 오픈 함수
def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output


# 파일 쓰기 함수
def writecsv(filename, the_list):
#     파일을 읽을 때 사용
    with open(filename, 'w', newline='') as f:
        a = csv.writer(f, delimiter=',')
        a.writerows(the_list)


# 문자 리스트 -> 실수 리스트 변환
# a = [['1','2','3'],['2','3',5']]
# b = switch(a)
# b = [[1.0,2.0,3.0],[2.0,3.0,5.0]]
def switch(listname):
    for i in listname:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return listname
