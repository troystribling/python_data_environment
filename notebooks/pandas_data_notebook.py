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
ca_biking['Berri1'].plot()

# %%
ca_biking.plot(figsize=(10, 6))

# %%
# Aggregating data
berri_bikes = ca_biking[['Berri1']]

# Add a weekday columnn
berri_bikes.iloc[berri_bikes['week_day']] = berri_bikes.index.weekday
