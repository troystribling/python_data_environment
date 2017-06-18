# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

%aimport numpy

from scipy.stats import beta
from examples import stats_plots

# %%
# Consider a coin with probability of throwing heads h. If h is unknown after n tosses with r heads the posterior
# probability of h determined from Bayes is Beta(r + 1, n - r + 1)
def coin_flip_posterior(h, n, r):
    return beta.pdf(h, n + 1, n - r + 1)

h = numpy.linspace(0.0, 1.0, 100)

# %%
stats_plots.pdf_plot(h, coin_flip_posterior(h, 500, 100))

# %%
stats_plots.pdf_plot(h, coin_flip_posterior(h, 500, 400))
