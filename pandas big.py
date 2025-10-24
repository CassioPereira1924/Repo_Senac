import pandas as pd

df_jan = pd.read_csv('jan.csv', sep= ';', encoding= 'latin1')
df_fev = pd.read_csv('fev.csv', sep= ';', encoding= 'latin1')
df_mar = pd.read_csv('mar.csv', sep= ';', encoding= 'latin1')
df_abr = pd.read_csv('abr.csv', sep= ';', encoding= 'latin1')
df_mai = pd.read_csv('mai.csv', sep= ';', encoding= 'latin1')
df_jun = pd.read_csv('jun.csv', sep= ';', encoding= 'latin1')
df_jul = pd.read_csv('jul.csv', sep= ';', encoding= 'latin1')
df_ago = pd.read_csv('ago.csv', sep= ';', encoding= 'latin1')

df = pd.concat([df_jan, df_fev, df_mar, df_abr, df_mai, df_jun, df_jul, df_ago], ignore_index= True)
print(df.head())
