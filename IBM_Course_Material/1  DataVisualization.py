import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

excelsheet = 'Canada.xlsx'

df_can = pd.read_excel(excelsheet, sheet_name="Candana by Citizenship",skiprows=range(20), skipfooter=2)

print(df.head())