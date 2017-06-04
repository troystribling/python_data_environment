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
