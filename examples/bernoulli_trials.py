import numpy
from scipy.stats import uniform
from scipy.stats import norm

def params_binomal_to_normal(p, n):
    μ = n * p
    σ = numpy.sqrt(n * p * (1.0 - p))
    return μ, σ

def params_estimate_success_probability(success_count, n):
    p = success_count / n
    σ = numpy.sqrt(p * (1.0 - p) / n)

def success_count_trial(p, n):
    success_count = 0
    for toss in uniform.rvs(size=n):
        if toss < p:
            success_count += 1
    return success_count

def success_count_trials(nexp, p, n):
    return [success_count_trial(p, n) for _ in range(nexp)]

def success_count_trial_outliers(alpha, trials, p, n):
    μ, σ = params_binomal_to_normal(p, n)
    acceptence_interval = norm.interval(alpha, μ, σ)
    return [trial for trial in trials if trial < acceptence_interval[0] or trial > acceptence_interval[1]]

# The probability that success_count is at least extreme as what was observed
def pvalue(observed_success_count, μ, σ):
    if observed_success_count > μ:
        # exterem values are in tail multiply by 2 for upper and lower ends of distribution
        return 2 * norm.sf(observed_success_count, μ, σ)
    else:
        # exterem values are less than tail multiply by 2 for upper and lower ends of distribution
        return 2 * norm.cdf(observed_success_count, μ, σ)
