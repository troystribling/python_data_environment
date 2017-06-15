# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

%aimport numpy

from scipy.stats import binom
from examples import stats_plots

# %%
x = numpy.linspace(0.0, 1.0, 100)
p = binom.pmf(10.0, 200.0, x)
stats_plots.pdf_plot(x, p)
