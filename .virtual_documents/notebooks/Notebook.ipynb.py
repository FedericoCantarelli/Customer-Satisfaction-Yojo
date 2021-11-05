# Import useful libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import numpy as np


df_raw = pd.read_csv('../data/raw/model.csv', index_col=0)
df_raw.head()


df_raw.dtypes


df_raw.isnull().any()


df_raw.info()


df_raw.isnull().sum()


msno.matrix(df_raw);
plt.savefig('../reports/figures/missing_matrix.png', dpi = 200)


categorical = ['Gender', 'Satisfaction', 'NewUsed', 'Category', 'Customer Type']
for lab in categorical:
    print('********')
    print(df_raw[lab].value_counts())


df_raw[df_raw.duplicated()]


sat = {'Not Satisfied':0,'Satisfied':1}
df_raw['Satisfaction'].replace(sat, inplace = True)
df_raw


df_raw.groupby(['Gender', 'Customer Type'])['Age'].mean()


df_proc_prem = pd.DataFrame(df_raw.loc[df_raw['Customer Type']=='Premium', :].fillna(round(df_raw.loc[df_raw['Customer Type']=='Premium', 'Age'].mean(),0)))
df_proc_com = pd.DataFrame(df_raw.loc[df_raw['Customer Type']=='Not Premium', :].fillna(round(df_raw.loc[df_raw['Customer Type']=='Not Premium', 'Age'].mean(),0)))


df_proc.isnull().sum()


df_proc.to_csv('../data/processed/model_cleaned.csv')


df_proc.groupby(['Gender', 'Customer Type'])['Age'].mean()



