# P.110

import numpy as np
# print(np.__version__)

ar1 = np.array([1, 2, 3, 4, 5])
# print(ar1)
# print(type(ar1))

# ar2 = np.array([[10, 20, 30], [40, 50, 60]])
# print(ar2)

# 1 ~ 11 까지의 증가값 2
ar3 = np.arange(1, 11, 2)
# print(ar3)

ar4 = np.arange(1, 31, 3)
# print(ar4)

# 배열 형태를 3행 2열로 구조 변경
ar5 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2))
# print(ar5)

ar6 = np.zeros((2, 3))
# print(ar6)

# index 0 부터 2개를 배열로 가져옴
ar7 = np.array([[10, 20, 30], [40, 50, 60]])
ar8 = ar7[0:2, 0:2]
# print(ar8)

ar9 = ar7[0:]
ar10 = ar7[0, :]
# print(ar9)
# print('-------')
# print(ar10)

# numpy 사칙연산
ar11 = np.array([1, 2, 3, 4, 5])
ar12 = ar11 + 10
# print(ar12)
ar13 = ar11 + ar12
# print(ar13)

ar14 = ar13 * 2
print(ar14)

