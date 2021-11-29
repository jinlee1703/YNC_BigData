import numpy as np
import pandas as pd

# 피처 이름 파일 읽어오기
feature_name_df = pd.read_csv('UCI HAR Dataset/features.txt', sep='\s+', header=None, names=['index', 'featue_name'], engine='python')
feature_name = feature_name_df.iloc[:, 1].values.tolist()

X_train = pd.read_csv('UCI HAR Dataset/train/X_train.txt', sep='\s+', names=feature_name, engine='python')
X_test = pd.read_csv('UCI HAR Dataset/test/X_test.txt', sep='\s+', names=feature_name, engine='python')

Y_train = pd.read_csv('UCI HAR Dataset/train/y_train.txt', sep='\s+', header=None, names=['action'], engine='python')
Y_test = pd.read_csv('UCI HAR Dataset/test/y_test.txt', sep='\s+', header=None, names=['action'], engine='python')

label_name_df = pd.read_csv('UCI HAR Dataset/activity_labels.txt', sep='\s+', header=None, names=['index', 'label'], engine='python')
label_name = label_name_df.iloc[:, 1].values.tolist()

from sklearn.tree import DecisionTreeClassifier

# 결정 트리 분류 분석: 모델 생성
dt_HAR = DecisionTreeClassifier(random_state=156)

# 결정 트리 분류 분석: 모델 훈련
dt_HAR.fit(X_train, Y_train)        # 오류 뜸

# 결정 트리 분류 ㅂ누석: 평가 데이터에 예측 수행 -> 예측 결과로 Y_predcit 구하기
Y_predict = dt_HAR.predict(X_test)

print(Y_predict)