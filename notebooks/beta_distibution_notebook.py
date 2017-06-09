# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

%aimport numpy

from scipy.stats import beta

from examples import stats_plots
from examples import bernoulli_trials

# The beta distribution is the continuos version of the binomial distribition where factorials are replaced by Γ(n)
# and the exponents for polynomials are not required to be integers. It is also only defined for 0 <= p <= 1 Where
# p the equivalent of the probability in the binomial distribution.
#   Β(α,β) = Γ(α)Γ(β)/Γ(α+β)
#   Beta(p,α,β) = [x^(α-1)][1-x]^(β-1)/Β(α,β)
# is the equivalent of
#   Binomial(p, n, m) = [(x^m)(1 - x)^(n-m)]n!/(n-m)!m!

# %%
# cdf is the cumlative distribution function
# For standard beta distribution the cdf approaches 1 as x ⇢ 1
beta.cdf(1.0, 0.5, 1.75)
beta.cdf(1.0, 2.25, 1.8)
beta.cdf(1.0, 2.75, 3.83)

# For the standard beta distribution the cdf approaches 0 as x ⇢ 0
beta.cdf(0.0, 1.5, 1.75)
beta.cdf(0.0, 2.25, 1.8)
beta.cdf(0.0, 2.75, 3.83)

# %%
# ppf is percentile point function which returns the value of the distribution at the specified percentile the
# inverse of the cdf
beta.ppf(0.5, 0.5, 1.75)
beta.ppf(0.5, 1.0, 1.0)

# %%
x = numpy.linspace(0.0, 1.0, 100)
beta_pdfs = [beta.pdf(x, 1.0, 1.0), beta.pdf(x, 1.5, 2.75), beta.pdf(x, 8.5, 3.75), beta.pdf(x, 10.0, 10.0)]
stats_plots.multi_line_pdf_plot(x, beta_pdfs)

# %%
x = numpy.linspace(0.0, 1.0, 100)
beta_cdfs = [beta.cdf(x, 1.0, 1.0), beta.cdf(x, 1.5, 2.75), beta.cdf(x, 8.5, 3.75),
             beta.cdf(x, 10.0, 10.0)]
stats_plots.multi_line_pdf_plot(x, beta_cdfs)

# %%
# The beta distribution is the conjugate prior of the binomial distribution for
# estimating the succes probability of a trial. The posterior distribution is given by

def beta_posterior(success_count, n, x, α, β):
    return beta.pdf(x, α + success_count, β + n - success_count)

## %%
# estimate probability for fair Bernouli trail using beta posterior with unform
# prior, α=1.0, β=1.0
p = 0.5
ns = [10, 100, 1000, 10000]
x = numpy.linspace(0.0, 1.0, 100)
success_counts = [bernoulli_trials.success_count_trial(p, n) for n in ns]
posterior_distributions = [beta_posterior(success_counts[i], ns[i], x, 1.0, 1.0) for i in range(len(ns))]
stats_plots.multi_line_pdf_plot(x, posterior_distributions)

## %%
# estimate probability for failing Bernouli trail using beta posterior with unform
# prior, α=1.0, β=1.0
p = 0.35
ns = [10, 100, 1000, 10000]
x = numpy.linspace(0.0, 1.0, 100)
success_counts = [bernoulli_trials.success_count_trial(p, n) for n in ns]
posterior_distributions = [beta_posterior(success_counts[i], ns[i], x, 1.0, 1.0) for i in range(len(ns))]
stats_plots.multi_line_pdf_plot(x, posterior_distributions)
