%matplotlib inline
%reload_ext autoreload
%autoreload 2

%aimport numpy
%aimport pandas
%aimport seaborn

from matplotlib import pyplot

# %%
# Read data from a data/ca_bikers.csv, parse the Date column to a Date object and make it an index
ca_biking_data_frame = pandas.read_csv('data/ca_bikers.csv', parse_dates=['Date'], dayfirst=True, index_col='Date')

# List first 3 columns
ca_biking_data_frame.iloc[:3]

ca_biking_data_frame.columns

ca_biking_data_frame['Berri1'][:3]

# %%
ca_biking_data_frame['Berri1'].plot()

# %%
ca_biking_data_frame.plot(figsize=(10, 6))

# %%
# Look at NYC 311 calls form quite a large file
complaints = pandas.read_csv('large_data/311_Service_Requests_from_2011.csv')
complaints.shape
len(complaints.index)

complaints.columns

complaints.iloc[0:3, :6]

complaints['Complaint Type'][:5]

complaints[['Complaint Type', 'Borough']][:5]

complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10]

complaint_counts[:10].plot(kind='bar', figsize=(8, 4))

# %%
is_noise = complaints['Complaint Type'] == 'Noise - Street/Sidewalk'
in_brookliyn = complaints['Borough'] == 'BROOKLYN'
complaints[is_noise][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:5]

complaints[is_noise & in_brookliyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:5]
