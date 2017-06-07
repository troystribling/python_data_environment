import matplotlib.pyplot as pyplot
from scipy import stats
import seaborn

def pdf_plot(x, y):
    seaborn.set(color_codes=True)
    pyplot.plot(x, y, linestyle = 'solid')
    pyplot.ylabel("PDF")

def cdf_plot(x, y):
    seaborn.set(color_codes=True)
    pyplot.plot(x, y, linestyle = 'solid')
    pyplot.ylabel("CDF")

def multi_line_pdf_plot(x, ys):
    seaborn.set(color_codes=True)
    for i in range(len(ys)):
        pyplot.plot(x, ys[i])
    pyplot.ylabel("PDF")

def multi_line_cdf_plot(x, ys):
    seaborn.set(color_codes=True)
    for i in range(len(ys)):
        pyplot.plot(x, ys[i])
    pyplot.ylabel("CDF")

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
