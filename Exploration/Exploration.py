# Chicago Crime Data Analysis 2012 -2017

import pandas as pd
from pandas import read_csv
crimes = read_csv("/home/zanesx/Desktop/CrimeRateInferenceWithBigData-master/Datasets for Chicago/Chicago_Crimes_2012_to_2017.csv", index_col='Date')

print(type(crimes))

crimes = crimes.iloc[:, 3: ]
crimes.head()

crimes.index = pd.to_datetime(crimes.index)

# print(crimes.shape)
print(crimes.head())

s = crimes[['Primary Type']]
s.head()
crime_count = pd.DataFrame(s.groupby('Primary Type').size().sort_values(ascending=False).rename('counts').reset_index())
crime_count.head()
crime_count.shape

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

# Initialize the matplotlib figure
# f, ax = plt.subplots(figsize=(4, 15))

# Plot the Number of crimes
sns.set_color_codes("pastel")
sns.barplot(x="counts", y="Primary Type", data=crime_count.iloc[:10, :],label="Total", color="b")

# ax.legend(ncol=2, loc="lower right", frameon=True)
# ax.set(ylabel="Type of Crime", xlabel="Number of Crimes")
# sns.despine(bottom=True, left=True)
# Add a legend and informative axis label
plt.title('Total Crimes')
plt.ylabel('Type of Crime')
plt.xlabel('Number of Crimes')
plt.show()

# Arrests
crimes_2012 = crimes.loc['2012']
crimes_2013 = crimes.loc['2013']
crimes_2014 = crimes.loc['2014']
crimes_2015 = crimes.loc['2015']
crimes_2016 = crimes.loc['2016']
crimes_2017 = crimes.loc['2017']

# Yearly crimes
arrest_yearly = crimes[crimes['Arrest'] == True]['Arrest']
plt.subplot()
# yearly arrest
arrest_yearly.resample('A').sum().plot()
plt.title('Yearly arrests')
plt.ylabel('Number of Arrests')
plt.xlabel('Year')
plt.show()

# Monthly arrest
arrest_yearly.resample('M').sum().plot()
plt.title('Monthly arrests')
plt.ylabel('Number of Arrests')
plt.xlabel('Month')
plt.show()

# Weekly arrest
arrest_yearly.resample('W').sum().plot()
plt.title('Weekly arrests')
plt.ylabel('Number of Arrests')
plt.xlabel('Week')
plt.show()

# daily arrest
arrest_yearly.resample('D').sum().plot()
plt.title('Daily arrests')
plt.ylabel('Number of Arrests')
plt.xlabel('Year')
plt.show()
plt.show()

#Top 5 crimes trend over the years

theft_2012 = pd.DataFrame(crimes_2012[crimes_2012['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
theft_2013 = pd.DataFrame(crimes_2013[crimes_2013['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
theft_2014 = pd.DataFrame(crimes_2014[crimes_2014['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
theft_2015 = pd.DataFrame(crimes_2015[crimes_2015['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
theft_2016 = pd.DataFrame(crimes_2016[crimes_2016['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])

grouper = theft_2012.groupby([pd.Grouper(freq='M'), 'Primary Type'])
grouper_2013 = theft_2013.groupby([pd.Grouper(freq='M'), 'Primary Type'])
grouper_2014 = theft_2014.groupby([pd.Grouper(freq='M'), 'Primary Type'])
grouper_2015 = theft_2015.groupby([pd.Grouper(freq='M'), 'Primary Type'])
grouper_2016 = theft_2016.groupby([pd.Grouper(freq='M'), 'Primary Type'])

data_2012 = grouper['Primary Type'].count().unstack()
data_2013 = grouper_2013['Primary Type'].count().unstack()
data_2014 = grouper_2014['Primary Type'].count().unstack()
data_2015 = grouper_2015['Primary Type'].count().unstack()
data_2016 = grouper_2016['Primary Type'].count().unstack()

#Monthly

data_2012.plot()
plt.title("Top 5 monthly crimes in 2012")
plt.ylabel('Number of Crimes')
plt.xlabel('Month')
plt.show()

data_2013.plot()
plt.title("Top 5 monthly crimes in 2013")
plt.ylabel('Number of Crimes')
plt.xlabel('Month')
plt.show()

data_2014.plot()
plt.title("Top 5 monthly crimes 2014")
plt.ylabel('Number of Crimes')
plt.xlabel('Month')
plt.show()

data_2015.plot()
plt.title("Top 5 monthly crimes 2015")
plt.ylabel('Number of Crimes')
plt.xlabel('Month')
plt.show()

data_2016.plot()
plt.title("Top 5 monthly crimes 2016")
plt.ylabel('Number of Crimes')
plt.xlabel('Month')
plt.show()
