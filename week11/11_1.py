import numpy as np
import pandas as pd

data_df = pd.read_csv('iris_data.csv', header=0, engine='python')

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

Y = data_df['class']
X = data_df.drop(['class'], axis=1, inplace=False)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
lr = LinearRegression()

lr.fit(X_train, Y_train)
Y_predict = lr.predict(X_test)

mse = mean_squared_error(Y_test, Y_predict)
rmse = np.sqrt(mse)
# print('MSE : {0:.3f}, RMSE : {1:.3f}'.format(mse, rmse))
# print('R^2(Variance score) : {0:.3f}'.format(r2_score(Y_test, Y_predict)))
#
# print('Y 절편 값: ', np.round(lr.intercept_, 2))
# print('회귀 계수 값: ', np.round(lr.coef_, 2))

print("연비를 예측하고 싶은 차의 정보를 입력해주세요.")
cylinders_1 = float(input("sepal_length : "))
displacement_1 = float(input("sepal_width : "))
weight_1 = float(input("petal_length : "))
acceleration_1 = float(input("petal_width : "))

mpg_predict = lr.predict([[cylinders_1, displacement_1, weight_1, acceleration_1]])
# print("이 자동차의 예상 연비(MPG)는 %.2f입니다." %mpg_predict)

if mpg_predict >= 5 and mpg_predict <= 15:
    print("예측한 iris data는 setosa입니다.")
elif mpg_predict >= 16 and mpg_predict <=25:
    print("예측한 iris data는 versicolor입니다.")
elif mpg_predict >= 25 and mpg_predict <= 35:
    print("예측한 iris data는 virginica입니다.")
