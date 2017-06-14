# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

import numpy
import pandas
from matplotlib import pyplot

# %%
# create a Series from an input list of values, letting pandas create a default integer index
series = pandas.Series([1, 3, 5, numpy.nan, 8, 8])

# Access different elments in series
series.iloc[0]
series.iloc[3]
series.iloc[5]

# Data from series in range 1, 2, 3
series.iloc[1:3]

# Last element in series
series.iloc[-1:]

# %%
# create a DataFrame by passing a numpy array, with a datetime index and labeled columns

# Make an array of six dates starting with 1/1/2013 incrementing by day
dates = pandas.date_range('20130101', periods=6, freq='D')

# Create data frame of random numbers
data_frame = pandas.DataFrame(numpy.random.randn(6,4), index=dates, columns=list('ABCD'))

# Access data by column name
data_frame.A
data_frame.B

# View head and tail of data_frame
data_frame.head(1)
data_frame.tail(2)

# View data_frame index columns
days = data_frame.index

# Display data_frame column names
data_frame.columns

# Display data_frame values
data_frame.values

# Display data in tabular output
data_frame.describe()

# Access data in data_frame by index
data_frame.loc[days[0]]

# Access data in data_frame using iloc by columns
data_frame.iloc[:,0]
data_frame.iloc[:, 1:3]

# Access data in data_frame using iloc by rows
data_frame[1:3]
