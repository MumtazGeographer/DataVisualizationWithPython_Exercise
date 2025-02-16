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

print(df_can.Country)

print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]) # returns a dataframe

#print(df.loc[label])
print(df_can.set_index('Country', inplace=True))

df_can.index.name = None
print(df_can.loc['Japan'])

print(df_can.iloc[87])

print(df_can[df_can.index == 'Japan'])

print(df_can.loc['Japan', 2013], " \n df_can.loc['Japan', 2013]")

# Alternative method
# year 2013 iw the last folumn with a positional inde of 36.
print(df_can.iloc[87, 36], " \n df_can.iloc[87, 36]")

# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984]])

# Alternative Method
print(df_can.iloc[87, [3,4,5,6,7,8]])

df_can.columns = list(map(str, df_can.columns))
print(df_can.columns)

# useful for plotting later on
years = list(map(str, range(1980, 2014)))


# FILTERING BASED ON A CRITERIA
condition = df_can['Continent'] == 'Asia'
print(condition)


# 2. pass this condition into the dataFrame
print(df_can[condition])


print(df_can[(df_can['Continent'] == 'Asia') & (df_can['Region']=='Southerrn Asia')])


print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)

# we are using the inline backend
#%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt

print(mpl.__version__)

print(plt.style.available)
print(mpl.style.use(['ggplot']))

haiti = df_can.loc['Haiti', years]
print(haiti.head())

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake.
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show()

df_CI = df_can.loc[['India', 'China'], years]
df_CI = df_CI.transpose()
df_CI.plot(kind='line')

plt.show()

# The correct answer is:
df_CI.index = df_CI.index.map(int)  # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()

# The correct answer is:
df_CI.index = df_CI.index.map(int)  # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()