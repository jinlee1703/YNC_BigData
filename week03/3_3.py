import matplotlib.pyplot as plt
from numpy.random import rand

# 라인플롯 차트 1
# x = [2016, 2017, 2018, 2019, 2020]
# y = [350, 410, 520, 695, 543]
#
# plt.plot(x, y)
# plt.title('Annual sales')
# plt.xlabel('years')
# plt.ylabel('sales')
# plt.show()

# 라인플롯 차트 2
# import numpy as np
# a = np.linspace(0, 10, 100)
# b = np.exp(-a)
# plt.plot(a, b)
# plt.show()

# 히스토그램
# from numpy.random import normal, random
# x = normal(size=200)
# plt.hist(x, bins=30)
# plt.show()

# 산점도
# a = rand(100)
# print(a)
# b = rand(100)
# print(b)
# plt.scatter(a, b)
# plt.show()

# 바 차트
y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
x = range(len(y1))

plt.bar(x, y1, width=0.7, color="blue")
plt.bar(x, y2, width=0.7, color="red", bottom=y1)

plt.title('Quartely sales')
plt.xlabel('Quarters')
plt.ylabel('sales')

xLabel = ['first', 'second', 'third', 'fourth']

plt.xticks(x, xLabel, fontsize=10)
plt.legend(['chairs', 'desks'])

plt.show()