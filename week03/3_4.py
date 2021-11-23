import pandas as pd

data1 = [10, 20, 30, 40, 50]
data2 = ['1반', '2반', '3반', '4반', '5반']

data_dic = {'year':[2018, 2019, 2020],
            'sales':[350, 480, 1099]}

#Series 자료형

sr1 = pd.Series(data1)  #int64

sr2 = pd.Series(data2)  #object

sr3 = pd.Series([101, 102, 103, 104, 105])
print(sr3)

sr4 = pd.Series(['월', '화', '수', '목', '금'])

sr5 = pd.Series(data1, index=[1000, 1001, 1002, 1003, 1004])

sr6 = pd.Series(data1, index=data2)

sr7 = pd.Series(data2, index=data1)

sr8 = pd.Series(data2, index=sr4)

#DataFrame 자료형

df1 = pd.DataFrame(data_dic)

df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]], index=['중간고사', '기말고사'], columns=data2[0:3])

data_df = [['20201101', 'Hong', '90', '95'],
           ['20201102', 'Kim', '93', '94'],
           ['20201103', 'Lee', '87', '97']]

df3 = pd.DataFrame(data_df)
df3.columns=['학번', '이름', '중간고사', '기말고사']

#print(df3.head(2)) #위에서부터 2개 행 조회
#print(df3.tail(2)) #아래에서부터 2개 행 조회
#print(df3['이름'])  #'이름' 칼럼만 조회

df3.to_csv('D:\\YNC_3_2\\BigData\\toCsv\\score.csv', header='False')
df4 = pd.read_csv('D:\\YNC_3_2\\BigData\\toCsv\\score.csv', encoding='utf-8', index_col=0, engine='python')
# print(df4)