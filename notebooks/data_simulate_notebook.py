# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

import numpy

from examples import stats_plots
from examples import data_simulate

# %%
x = numpy.linspace(0.0, 100.0, 100)
spectrum = data_simulate.gaussian_spectrum([20.0, 60.0], [10.0, 5.0], [10.0, 20.0], x)
stats_plots.time_series_plot(x, spectrum)
