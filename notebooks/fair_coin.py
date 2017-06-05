# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

import numpy
from scipy.stats import norm
from scipy.stats import uniform

from examples import stats_plots
from examples import bernoulli_trials

# %%
n = 1000
p = 0.5
μ, σ = bernoulli_trials.params_binomal_to_normal(p, n)
bernoulli_trials.pvalue(500, μ, σ)
trails = bernoulli_trials.heads_count_trials(1000, p, n)
stats_plots.fit_dist_plot(trails, norm)

# %%
n = 1000
p = 0.45
μ, σ =  bernoulli_trials.params_binomal_to_normal(p, n)
bernoulli_trials.pvalue(500, μ, σ)
trails = bernoulli_trials.heads_count_trials(1000, p, n)
stats_plots.fit_dist_plot(trails, norm)
