import pandas as pd

red_df = pd.read_csv('D:\YNC_3_2\BigData\wine\winequality-red.csv', sep=';', header=0, engine='python')
white_df = pd.read_csv('D:\YNC_3_2\BigData\wine\winequality-white.csv', sep=';', header=0, engine='python')

#red_df.to_csv('D:\YNC_3_2\BigData\wine\winequality-red2.csv', index=False)
#white_df.to_csv('D:\YNC_3_2\BigData\wine\winequality-white2.csv', index=False)

red_df.insert(0, column='type', value='red')
white_df.insert(0, column='type', value='white')

wine = pd.concat([red_df, white_df])
#wine.to_csv('D:\YNC_3_2\BigData\wine\wine.csv', index=False)

wine.columns = wine.columns.str.replace(' ', '_')

#--------------------------------------------------------------------------------

from scipy import stats
from statsmodels.formula.api import ols, glm

red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']
#print(stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var=False))
Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + ' \
           'free_sulfur_dioxide + total_sulfur_dioxide + ' \
           'density + pH + sulphates + alcohol'
regression_result = ols(Rformula, data=wine).fit()

sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]
sample1_predict = regression_result.predict(sample1)


#--------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('dark')
sns.distplot(red_wine_quality, kde=True, color='red', label='red wine')
sns.distplot(white_wine_quality, kde=True, label='white wine')
plt.title("Quality of Wine Type")
plt.legend()

import statsmodels.api as sm
others = list

