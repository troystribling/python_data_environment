# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 1

%aimport numpy

from scipy.stats import norm as norm

import examples.stats_plots as stats_plots

# %% ppf is percentile point function which returns the
# value of the distribution at the specified percentile

# percentile for mean
norm.ppf(0.5)

# percentile for positive one standard deviation
norm.ppf(0.841)

# percentile for one negative standard deviation
norm.ppf(0.159)

# %% plot standard normal pdf
x = numpy.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
stats_plots.pdf_plot(x, norm.pdf(x))

# %% generate standard normal random variables and plot kde
norm_rvs = norm.rvs(size=100)
stats_plots.dist_plot(norm_rvs)

stats_plots.normal_fit_plot(norm_rvs)
