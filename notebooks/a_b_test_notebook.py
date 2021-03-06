# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

import numpy
from scipy.stats import norm

from examples import stats_plots
from examples import bernoulli_trials

# %%
# A/B trial test statistic is derived from the the difference of the trial probability estimate
# s = (μa - μb)/sqrt(σa**2 + σb**2) which is assumed to be normally distributed with mean 0 and
# varaince 1 as a consequence of the bernoulli trial having a binomial distribution which is approximately
# normal for large n. This statistic is a statement of the null hypothesis for the two trials. The
# null hypothesis is that the difference between the trails will only be due to its random nature.
def a_b_test_statistic(μa, σa, μb, σb):
    return (μa - μb)/numpy.sqrt(σa**2 + σb**2)

# %%
# Run an A/B Bernoului Trial test with pa = pb
pa = 0.5
pb = pa
na = 1000
nb = 2000
success_count_trial_a = bernoulli_trials.success_count_trial(pa, na)
μa, σa = bernoulli_trials.params_estimate_probability(success_count_trial_a, na)

success_count_trial_b = bernoulli_trials.success_count_trial(pb, nb)
μb, σb = bernoulli_trials.params_estimate_probability(success_count_trial_b, nb)

test_stat = a_b_test_statistic(μa, σa, μb, σb)

# verify that the null hypothesis is staisified by verifying that the result is within the 95%
# confidence interval.
bernoulli_trials.pvalue(test_stat, 0.0, 1.0)

# %%
# Run an A/B test with pa < pb
pa = 0.45
pb = 0.5
na = 1000
nb = 1500

success_count_trial_a = bernoulli_trials.success_count_trial(pa, na)
μa, σa = bernoulli_trials.params_estimate_probability(success_count_trial_a, na)

success_count_trial_b = bernoulli_trials.success_count_trial(pb, nb)
μb, σb = bernoulli_trials.params_estimate_probability(success_count_trial_b, nb)

test_stat = a_b_test_statistic(μa, σa, μb, σb)

# verify that the null hypothesis is staisified by verifying that the result is within the 95%
# confidence interval.
bernoulli_trials.pvalue(test_stat, 0.0, 1.0)
