from scipy.stats import norm
import math
import numpy

def binomial_to_normal(p, n):
    μ = n * p
    σ = numpy.sqrt(n * p (1 - p))
    return μ, σ

def normal_cdf(x, μ, σ):
    return norm.cdf(x, μ, math.pow(σ, 2))

def normal_tail(x, μ, σ):
    return 1.0 - normal_cdf(x, μ, σ)

def normal_interval(x, y, μ, σ):
    return normal_cdf(y, μ, σ) - normal_cdf(x, μ, σ)

def normal_outside_interval(x, y, μ, σ):
    return 1.0 - normal_interval(x, y, μ, σ)
