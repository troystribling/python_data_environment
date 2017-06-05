# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

import numpy
from scipy.stats import norm
from scipy.stats import uniform

from examples import stats_plots

# %%
def binomal_params_to_normal(p, n):
    μ = n * p
    σ = numpy.sqrt(n * p * (1.0 - p))
    return μ, σ

def heads_count_generate(p, n):
    heads = 0
    for toss in uniform.rvs(size=n):
        if toss < p:
            heads += 1
    return heads

# %%
n = 1000
fair_coin = 0.5
winning_coin = 0.55
losing_coin = 0.45

fair_coin_heads_count = heads_count_generate(fair_coin, n)
winning_coin_heads_count = heads_count_generate(winning_coin, n)
losing_coin_heads_count = heads_count_generate(losing_coin, n)

fair_coin_μ, fair_coin_σ = binomal_params_to_normal(fair_coin, n)
winning_coin_μ, winning_coin_σ = binomal_params_to_normal(winning_coin, n)
losing_coin_μ, losing_coin_σ = binomal_params_to_normal(losing_coin, n)

fair_coin_confidence_interval = norm.interval(0.95, fair_coin_μ, fair_coin_σ)
winning_coin_confidence_interval = norm.interval(0.95, winning_coin_μ, winning_coin_σ)
losing_coin_confidence_interval = norm.interval(0.95, losing_coin_μ, losing_coin_σ)
