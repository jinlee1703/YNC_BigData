import numpy as np

ar1 = np.array([1, 2, 3, 4, 5])

ar2 = np.array([[10, 20, 30], [40, 50, 60]])

ar3 = np.arange(1, 11, 2)

ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2))      #.reshape(3, 2)와 결과가 같음

ar5 = np.zeros((2, 3))                                  #.zeros(2, 3) 시 오류 발생

ar6 = ar2[0:2, 0:2]

ar7 = ar2[0, :]                                         #ar7 = ar2[0]와 결과가 같음

ar8 = ar1 + 10
#print(ar1 + ar8)                                       #[1 2 3 4 5] + [11 + 12 + 13 + 14 + 15]
#print(ar8 - ar1)                                       #[11 + 12 + 13 + 14 + 15] - [1 2 3 4 5]
#print(ar1 * 2)                                         #[1 2 3 4 5] * 2
#print(ar1 / 2)                                         #[1 2 3 4 5] / 2

#ar2는 2x3 행렬[[10, 20, 30], [40, 50, 60]] / ar4는 3x2 행렬[[1, 2], [3, 4], [5, 6]]
ar9 = np.dot(ar2, ar4)                                  #행렬 곱셈을 할 때는 a(아무숫자) x n 행렬일 때는 n x b(아무 숫자) 행렬이여야 곱할 수 있고 결과는 axb 행렬이 출력
print(ar9)                                              #영상 3_1 참고