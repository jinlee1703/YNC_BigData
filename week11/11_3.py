import numpy as np
import pandas as pd


# 피처 이름 파일 읽어오기
feature_name_df = pd.read_csv('UCI HAR Dataset/features.txt', sep='\s+', header=None, names=['index', 'feature_name'], engine='python')
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

# 결정 트리 분류 분석: 평가 데이터에 예측 수행 -> 예측 결과로 Y_predcit 구하기
Y_predict = dt_HAR.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(Y_test, Y_predict)
print('결정 트리 예측 정확도: {0:.4f}'.format(accuracy))
print('결정 트리의 현재 하이퍼 매개변수: \n', dt_HAR.get_params())

from sklearn.model_selection import GridSearchCV
params = {
    'max_depth': [6, 8, 10, 12, 16, 20, 24]
}

grid_cv = GridSearchCV(dt_HAR, param_grid=params, scoring='accuracy', cv=5, return_train_score=True)

grid_cv.fit(X_train, Y_train)

GridSearchCV(cv=5, estimator=DecisionTreeClassifier(random_state=156), param_grid={'max_depth': [6, 8, 10, 12, 16, 20, 24]}, return_train_score=True, scoring='accuracy')

cv_result_df = pd.DataFrame(grid_cv.cv_results_)
cv_result_df[['param_max_depth', 'mean_test_score', 'mean_train_score']]
print('최고 평균 정확도: {0:.4f}, 최적 하이퍼 매개변수: {1}'.format(grid_cv.best_score_, grid_cv.best_params_))

params = {
    'max_depth': [8, 16, 20],
    'min_samples_split': [8, 16, 24]
}

grid_cv = GridSearchCV(dt_HAR, param_grid=params, scoring='accuracy', cv=5, return_train_score=True)

grid_cv.fit(X_train, Y_train)
cv_result_df = pd.DataFrame(grid_cv.cv_results_)
cv_result_df[['param_max_depth', 'param_min_samples_split', 'mean_test_score', 'mean_train_score']]
print('최고 평균 정확도: {0:.4f}, 최적 하이퍼 매개변수: {1}'.format(grid_cv.best_score_, grid_cv.best_params_))

best_dt_HAR = grid_cv.best_estimator_
best_Y_predict = best_dt_HAR.predict(X_test)
best_accuracy = accuracy_score(Y_test, best_Y_predict)
print('best 결정 트리 예측 정확도: {0:.4f}'.format(best_accuracy))

import seaborn as sns
import matplotlib.pyplot as plt

feature_importance_values = best_dt_HAR.feature_importances_
feature_importance_values_s = pd.Series(feature_importance_values, index=X_train.columns)
feature_top10 = feature_importance_values_s.sort_values(ascending=False)[:10]

plt.figure(figsize=(10, 5))
plt.title('Feature Top 10')
sns.barplot(x=feature_top10, y=feature_top10.index)
plt.show()
