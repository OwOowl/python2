import pandas as pd

data_dic = {
    'year':[2018, 2019, 2020],
    'sales':[350, 480, 1099]
}
# print(data_dic)

# 표 형태로 출력
dt1 = pd.DataFrame(data_dic)
# print(dt1)


data2 = ['1반', '2반', '3반', '4반', '5반']
dt2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]], index=['중간고사', '기말고사'], columns=data2[0:3])
# print(dt2)

data_df = [['20201101', 'Hong', '90', '95'], ['20201102',
'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)
# print(df3)
df3.columns = ['학번', '이름', '중간고사', '기말고사']
# print(df3)

# print(df3.head(2))
# print(df3.tail(2))
# print(df3['이름'])

df3.to_csv('./data/score.csv', header=True, encoding='utf-8-sig')
df3.to_csv('./data/score1.csv', header=False, encoding='utf-8-sig')

df4 = pd.read_csv('./data/score.csv', encoding='utf-8', index_col=0)
print(df4)

