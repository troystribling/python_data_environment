import numpy
from scipy.stats import uniform
from scipy.stats import norm

def params_binomal_to_normal(p, n):
    μ = n * p
    σ = numpy.sqrt(n * p * (1.0 - p))
    return μ, σ

def heads_count_trial(p, n):
    heads_count = 0
    for toss in uniform.rvs(size=n):
        if toss < p:
            heads_count += 1
    return heads_count

def heads_count_trials(nexp, p, n):
    heads_count = []
    for _ in range(nexp):
        heads_count.append(heads_count_trial(p, n))
    return heads_count

# The probability that heads_count is at least extreme as what was observed
def pvalue(observed_heads_count, μ, σ):
    if observed_heads_count > μ:
        # exterem values are in tail multiply by 2 for upper and lower ends of distribution
        return 2 * norm.sf(observed_heads_count, μ, σ)
    else:
        # exterem values are less than tail multiply by 2 for upper and lower ends of distribution
        return 2 * norm.cdf(observed_heads_count, μ, σ)
