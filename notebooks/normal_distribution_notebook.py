# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

%aimport numpy

from scipy.stats import norm
from examples import stats_plots

# %%
# cdf is the cumlative distribution function
# For standard nomal distribution the cdf approaches 1 as x ⇢ ∞
norm.cdf(1000.0)

# For the standard normal distribution the cdf approaches 0 as x ⇢ -∞
norm.cdf(-1000.0)

# For the standard normal distribution the cdf of the mean is 0.5
norm.cdf(0.0)

# For the standard normal distribution the cdf 1 standard deviation positive of the mean is
norm.cdf(1.0)

# The tail probability or survival function for the standard normal distribution 1 standard
# deviation positive of the mean is given by
1.0 - norm.cdf(1.0)
norm.sf(1.0)

# %%
# ppf is percentile point function which returns the value of the distribution at the
# specified percentile the inverse of the cdf

# percentile for mean of standard normal distribution
norm.ppf(0.5)

# percentile for positive one standard deviation of standard normal distribution
norm.ppf(0.841)

# percentile for one negative standard deviation of standard normal distribution
norm.ppf(0.159)
norm.ppf(norm.cdf(1.0))

# The inverse of the survival function for the standard normal distribution 1 standard
# deviation positive of the mean is given by
norm.isf(0.158)
norm.isf(norm.sf(1.0))

# %%
# The probability of a standard normal random lying in the interval 1 standard deviation
# from the mean is
norm.cdf(1.0) - norm.cdf(-1.0)
norm.sf(-1.0) - norm.sf(1.0)

# The inverse of the interval probability assuming symetry about the mean is
norm.interval(0.683)

# %%
# Plot standard normal pdf
x = numpy.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
stats_plots.pdf_plot(x, norm.pdf(x))

# %%
# Generate standard normal random variables and plot kde
norm_rvs = norm.rvs(size=1000)
stats_plots.dist_plot(norm_rvs)

# %%
stats_plots.normal_fit_plot(norm_rvs)
