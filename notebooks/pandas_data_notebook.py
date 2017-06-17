# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

%aimport numpy
%aimport pandas
%aimport seaborn

from matplotlib import pyplot

# %%
# Read data from a data/ca_bikers.csv, parse the Date column to a Date object and make it an index
ca_biking = pandas.read_csv('data/ca_bikers.csv', parse_dates=['Date'], dayfirst=True, index_col='Date')

# List first 3 columns
ca_biking.iloc[:3]

ca_biking.columns

ca_biking['Berri1'][:3]

# %%
berri_bikes = ca_biking[['Berri1']].copy()
berri_bikes.plot()

# %%
ca_biking.plot(figsize=(10, 6))

# %%
# Aggregating data
# Add a weekday columnn and do weekday sums
berri_bikes['weekday'] = berri_bikes.index.weekday

weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.plot(kind='bar')
