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
trials = bernoulli_trials.success_count_trials(1000, p, n)
outliers = bernoulli_trials.success_count_trial_outliers(0.95, trials, p, n)
outlier_probability = len(outliers) / len(trials)
stats_plots.fit_dist_plot(trails, norm)

# %%
n = 1000
p = 0.45
μ, σ =  bernoulli_trials.params_binomal_to_normal(p, n)
bernoulli_trials.pvalue(500, μ, σ)
trails = bernoulli_trials.success_count_trials(1000, p, n)
stats_plots.fit_dist_plot(trails, norm)
