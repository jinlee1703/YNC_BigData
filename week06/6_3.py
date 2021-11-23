import seaborn as sns
import pandas as pd

titanic = sns.load_dataset("titanic")
# titanic.to_csv('D:/YNC_3_2/BigData/toCsv/titanic.csv', index=False)
# print(titanic.isnull().sum())
titanic['age'] = titanic['age'].fillna(titanic['age'].median())
# print(titanic['embarked'].value_counts())
titanic['embarked'] = titanic['embarked'].fillna('S')
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
# print(titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')
# print(titanic.isnull().sum())
# print(titanic.info())
# print(titanic.survived.value_counts())

# import matplotlib.pyplot as plt
# f, ax = plt.subplots(1, 2, figsize=(10, 5))
# titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.\
#     pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
# titanic['survived'][titanic['sex'] == 'female'].value_counts().plot.\
#     pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
# ax[0].set_title('Survived (Male)')
# ax[1].set_title('Survived (FeMale)')
# plt.show()

# import matplotlib.pyplot as plt
#
# sns.countplot('pclass', hue='survived', data=titanic)
# plt.title('Pclass vs Survived')
# plt.show()

# titanic_corr = titanic.corr(method='pearson')
# titanic_corr.to_csv('D:/YNC_3_2/BigData/toCsv/titanic_corr.csv', index=False)

# print(titanic['survived'].corr(titanic['adult_male']))

import matplotlib.pyplot as plt

titanic_copy = pd.read_csv('D:/YNC_3_2/BigData/toCsv/titanic_copy.csv', header=0, engine='python')
# iris = sns.load_dataset('iris')
# sns.pairplot(iris)
sns.pairplot(titanic_copy, hue='survived')
plt.show()

