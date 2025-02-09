import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

excelsheet = 'Canada.xlsx'

#df_can = pd.read_excel(excelsheet, sheet_name="Candana by Citizenship",skiprows=range(20), skipfooter=2)
df_can = pd.read_excel(excelsheet, sheet_name="Canada by Citizenship", skiprows=range(20), skipfooter=2)
print(df_can.head())

print(df_can.tail())

print(df_can.info())

print(df_can.columns)

print(df_can.index)

print(type(df_can.columns))
print(type(df_can.index))

print(df_can.columns.tolist())
print(df_can.index.tolist())

print(df_can.shape)

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(2))

df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'},inplace=True)
print(df_can.columns)

#df_can['Total'] = df_can.sum(axis=1)
print(df_can.isnull().sum())

print(df_can.describe())
