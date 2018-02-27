#cell 0
# Chicago Crime Data Analysis

#cell 1
## Quick lookup

#cell 2
import pandas as pd
from pandas import read_csv
crimes = read_csv("/home/zanesx/Desktop/Datasets/Datasets for Demo/Chicago_Crimes_2012_to_2017.csv", index_col='Date')

#cell 3
print(type(crimes))

#cell 4
crimes = crimes.iloc[:, 3: ]
crimes.head()

#cell 5
crimes.index = pd.to_datetime(crimes.index)

#cell 6
print(crimes.shape)
print(crimes.head())

#cell 7
s = crimes[['Primary Type']]

#cell 8
s.head()

#cell 9
crime_count = pd.DataFrame(s.groupby('Primary Type').size().sort_values(ascending=False).rename('counts').reset_index())

#cell 10
crime_count.head()

#cell 11
crime_count.shape

#cell 12
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))


# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="counts", y="Primary Type", data=crime_count.iloc[:10, :],
            label="Total", color="b")

ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(ylabel="Type",
       xlabel="Crimes")
sns.despine(left=True, bottom=True)

# Add a legend and informative axis label
#plt.show()




#cell 13
## Arrests

#cell 14
crimes_2012 = crimes.loc['2012']
crimes_2013 = crimes.loc['2013']
crimes_2014 = crimes.loc['2014']
crimes_2015 = crimes.loc['2015']
crimes_2016 = crimes.loc['2016']
crimes_2017 = crimes.loc['2017']

## Yearly crimes
arrest_yearly = crimes[crimes['Arrest'] == True]['Arrest']

#cell 15
print(arrest_yearly.head())

#cell 16
plt.subplot()
# yearly arrest
arrest_yearly.resample('A').sum().plot()
plt.title('Yearly arrests')
plt.show()
# Monthly arrest
arrest_yearly.resample('M').sum().plot()
plt.title('Monthly arrests')
plt.show()
# Weekly arrest
arrest_yearly.resample('W').sum().plot()
plt.title('Weekly arrests')
plt.show()
# daily arrest
arrest_yearly.resample('D').sum().plot()
plt.title('Daily arrests')
plt.show()
plt.show()

#cell 17
## Domestic violence

#cell 18
domestic_yearly = crimes[crimes['Domestic'] == True]['Domestic']
print(domestic_yearly.head())

#cell 19

plt.subplot()
# yearly domestic violence
domestic_yearly.resample('A').sum().plot()
plt.title('Yearly domestic violence')
plt.show()
# Monthly domestic violence
domestic_yearly.resample('M').sum().plot()
plt.title('Monthly domestic violence')
plt.show()
# Weekly domestic violence
domestic_yearly.resample('W').sum().plot()
plt.title('Weekly domestic violence')
plt.show()
# daily domestic violence
domestic_yearly.resample('D').sum().plot()
plt.title('Daily domestic violence')
plt.show()
plt.show()

# #cell 20
# ## Top 5 crimes trend over the years
#
# #cell 21
# ### Monthly
#
# #cell 22
# theft_2012 = pd.DataFrame(crimes_2012[crimes_2012['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
# theft_2013 = pd.DataFrame(crimes_2013[crimes_2013['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
# theft_2014 = pd.DataFrame(crimes_2014[crimes_2014['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
# theft_2015 = pd.DataFrame(crimes_2015[crimes_2015['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
# theft_2016 = pd.DataFrame(crimes_2016[crimes_2016['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])

# #cell 23
# grouper = theft_2012.groupby([pd.TimeGrouper('M'), 'Primary Type'])
# grouper_2013 = theft_2013.groupby([pd.TimeGrouper('M'), 'Primary Type'])
# grouper_2014 = theft_2014.groupby([pd.TimeGrouper('M'), 'Primary Type'])
# grouper_2015 = theft_2015.groupby([pd.TimeGrouper('M'), 'Primary Type'])
# grouper_2016 = theft_2016.groupby([pd.TimeGrouper('M'), 'Primary Type'])
#
# #cell 24
# data_2012 = grouper['Primary Type'].count().unstack()
# data_2013 = grouper_2013['Primary Type'].count().unstack()
# data_2014 = grouper_2014['Primary Type'].count().unstack()
# data_2015 = grouper_2015['Primary Type'].count().unstack()
# data_2016 = grouper_2016['Primary Type'].count().unstack()
#
# #cell 25
# data_2012.plot()
# plt.title("Top 5 monthly crimes in 2012")
# plt.show()
#
# #cell 26
# data_2013.plot()
# plt.title("Top 5 monthly crimes in 2013")
# plt.show()
#
# #cell 27
# data_2014.plot()
# plt.title("Top 5 monthly crimes 2014")
# plt.show()
#
# #cell 28
# data_2015.plot()
# plt.title("Top 5 monthly crimes 2015")
# plt.show()
#
# #cell 29
# data_2016.plot()
# plt.title("Top 5 monthly crimes 2016")
# plt.show()

# #cell 30
# ###  Weekly
#
# #cell 31
# grouper = theft_2012.groupby([pd.TimeGrouper('W'), 'Primary Type'])
# grouper_2013 = theft_2013.groupby([pd.TimeGrouper('W'), 'Primary Type'])
# grouper_2014 = theft_2014.groupby([pd.TimeGrouper('W'), 'Primary Type'])
# grouper_2015 = theft_2015.groupby([pd.TimeGrouper('W'), 'Primary Type'])
# grouper_2016 = theft_2016.groupby([pd.TimeGrouper('W'), 'Primary Type'])
#
# data_2012 = grouper['Primary Type'].count().unstack()
# data_2013 = grouper_2013['Primary Type'].count().unstack()
# data_2014 = grouper_2014['Primary Type'].count().unstack()
# data_2015 = grouper_2015['Primary Type'].count().unstack()
# data_2016 = grouper_2016['Primary Type'].count().unstack()
#
# #cell 32
# data_2012.plot()
# plt.title("Top 5 Weekly crimes 2012")
# plt.show()
#
# #cell 33
# data_2013.plot()
# plt.title("Top 5 Weekly crimes 2013")
# plt.show()
#
# #cell 34
# data_2014.plot()
# plt.title("Top 5 Weekly crimes 2014")
# plt.show()
#
# #cell 35
# data_2015.plot()
# plt.title("Top 5 Weekly crimes 2015")
# plt.show()
#
# #cell 36
# data_2016.plot()
# plt.title("Top 5 Weekly crimes 2016")
# plt.show()

#cell 37
### Daily

# #cell 38
# grouper = theft_2012.groupby([pd.TimeGrouper('D'), 'Primary Type'])
# grouper_2013 = theft_2013.groupby([pd.TimeGrouper('D'), 'Primary Type'])
# grouper_2014 = theft_2014.groupby([pd.TimeGrouper('D'), 'Primary Type'])
# grouper_2015 = theft_2015.groupby([pd.TimeGrouper('D'), 'Primary Type'])
# grouper_2016 = theft_2016.groupby([pd.TimeGrouper('D'), 'Primary Type'])

# data_2012 = grouper['Primary Type'].count().unstack()
# data_2013 = grouper_2013['Primary Type'].count().unstack()
# data_2014 = grouper_2014['Primary Type'].count().unstack()
# data_2015 = grouper_2015['Primary Type'].count().unstack()
# data_2016 = grouper_2016['Primary Type'].count().unstack()

# #cell 39
# data_2012.plot()
# plt.title("Top 5 daily crimes 2012")
# plt.show()
#
# #cell 40
# data_2013.plot()
# plt.title("Top 5 daily crimes 2013")
# plt.show()
#
# #cell 41
# data_2014.plot()
# plt.title("Top 5 daily crimes 2014")
# plt.show()
#
# #cell 42
# data_2015.plot()
# plt.title("Top 5 daily crimes 2015")
# plt.show()
#
# #cell 43
# data_2016.plot()
# plt.title("Top 5 daily crimes 2016")
# plt.show()
