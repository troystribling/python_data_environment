import matplotlib.pyplot as pyplot
from scipy import stats
import seaborn

def pdf_plot(x, y):
    pyplot.plot(x, y, linestyle = 'solid')
    pyplot.ylabel("Probability")

def dist_plot(samples):
    seaborn.set(color_codes=True)
    seaborn.distplot(samples)

def histogram(samples, bins=None):
    seaborn.set(color_codes=True)
    seaborn.distplot(samples, kde=False, rug=True, bins=bins)

def fit_dist_plot(samples, stats):
    seaborn.set(color_codes=True)
    axes = seaborn.distplot(samples, fit=stats)
    (μ, σ) = stats.fit(samples)
    axes.text(0.75, 0.9, "μ=%d, σ=%d"%(μ, σ), transform=axes.transAxes)
