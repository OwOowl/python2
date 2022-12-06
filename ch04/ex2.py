import pandas as pd
# print(pd.__version__)

data1 = [10, 20, 30, 40, 50]
data2 = ['1반', '2반', '3반', '4반', '5반']
sr1 = pd.Series(data1)
# print(sr1)
sr2 = pd.Series(data2)
# print(sr2)

sr3 = pd.Series([101, 102, 103, 104, 105])
sr4 = pd.Series(['월', '화', '수', '목', '금'])

sr5 = pd.Series(data1, index=[1001, 1002, 1003, 1004, 1005])
# print(sr5)

sr6 = pd.Series(data1, index=data2)
# print(sr6)

sr7 = pd.Series(data2, index=sr4)
# print(sr7)
# print(sr7[2])   # 자리값 index
# print(sr7['수']) # 지정한 index 값
# print(sr7[-1])
# print(sr7[0:4])
# print(sr7.index)
# print(sr7.values)

# print(sr1 + sr3)
# print(sr4 + sr2)

