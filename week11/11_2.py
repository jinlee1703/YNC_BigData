import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer

b_cancer = load_breast_cancer()

b_cancer_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)
b_cancer_df['diagnosis'] = b_cancer.target

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# X, Y 설정하기
Y = b_cancer_df['diagnosis']
X = b_cancer_scaled

# 훈련용 데이터와 평가용 데이터 분할하기
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# 로지스틱 회귀 분석: (1) 모델 생성
lr_b_cancer = LogisticRegression()

# 로지스틱 회귀 분석: (2) 모델 훈련
lr_b_cancer.fit(X_train, Y_train)

# 로지스틱 회귀 분석: (3) 평가 데이터에 대한 예측 수행 ->> 예측 결과 Y_predict 구하기
Y_predict = lr_b_cancer.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

# 오차 행렬
confusion_matrix(Y_test, Y_predict)
accuracy = accuracy_score(Y_test, Y_predict)
precision = precision_score(Y_test, Y_predict)
recall = recall_score(Y_test, Y_predict)
f1 = f1_score(Y_test, Y_predict)
roc_auc = roc_auc_score(Y_test, Y_predict)

print('정확도: {0:.3f}, 정밀도: {1:.3f}, 재혀율: {2:.3f}, F1: {3:.3f}'.format(accuracy, precision, recall, f1))
print('ROC_AUC: {0:.3f}'.format(roc_auc))