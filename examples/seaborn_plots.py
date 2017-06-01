import numpy
import matplotlib.pyplot as pyplot
from scipy.stats import kendalltau
from string import ascii_uppercase
import pandas
import seaborn

def line_plots():
    seaborn.set(style="ticks")
    data_frame = seaborn.load_dataset("anscombe")
    seaborn.lmplot(x="x", y="y", col="dataset", hue="dataset", data=data_frame,
                   col_wrap=2, ci=None, palette="muted", size=4, scatter_kws={"s": 50, "alpha": 1})
def polar_plot():
    seaborn.set()
    r = numpy.linspace(0, 10, num=100)
    data_frame = pandas.DataFrame({'r': r, 'slow': r, 'medium': 2 * r, 'fast': 4 * r})
    data_frame = pandas.melt(data_frame, id_vars=['r'], var_name='speed', value_name='theta')
    g = seaborn.FacetGrid(data_frame, col="speed", hue="speed", subplot_kws=dict(projection='polar'), size=4.5, sharex=False, sharey=False, despine=False)
    g.map(pyplot.scatter, "theta", "r")

def distribution_plot():
    seaborn.set(style="white", palette="muted", color_codes=True)
    rs = numpy.random.RandomState(10)

    _, axis = pyplot.subplots(2, 2, figsize=(7, 7), sharex=True)
    seaborn.despine(left=True)

    d = rs.normal(size=100)

    seaborn.distplot(d, kde=False, color="b", ax=axis[0, 0])
    seaborn.distplot(d, hist=False, rug=True, color="r", ax=axis[0, 1])
    seaborn.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axis[1, 0])
    seaborn.distplot(d, color="m", ax=axis[1, 1])

    pyplot.setp(axis, yticks=[])
    pyplot.tight_layout()

def marginal_distribution_plot():
    seaborn.set(style="ticks")
    rs = numpy.random.RandomState(11)
    x = rs.gamma(2, size=1000)
    y = -.5 * x + rs.normal(size=1000)
    seaborn.jointplot(x, y, kind="hex", stat_func=kendalltau, color="#4CB391")

def scatter_plot_matrix():
    seaborn.set()
    data_frame = seaborn.load_dataset("iris")
    seaborn.pairplot(data_frame, hue="species")

def bivariate_kde_plot():
    seaborn.set(style="darkgrid")
    iris = seaborn.load_dataset("iris")

    # Subset the iris dataset by species
    setosa = iris.query("species == 'setosa'")
    virginica = iris.query("species == 'virginica'")

    # Set up the figure
    _, axis = pyplot.subplots(figsize=(8, 8))
    axis.set_aspect("equal")

    # Draw the two density plots
    axis = seaborn.kdeplot(setosa.sepal_width, setosa.sepal_length, cmap="Reds", shade=True, shade_lowest=False)
    axis = seaborn.kdeplot(virginica.sepal_width, virginica.sepal_length, cmap="Blues", shade=True, shade_lowest=False)

    # Add labels to the plot
    red = seaborn.color_palette("Reds")[-2]
    blue = seaborn.color_palette("Blues")[-2]
    axis.text(2.5, 8.2, "virginica", size=16, color=blue)
    axis.text(3.8, 4.5, "setosa", size=16, color=red)

def multiple_linear_regression_plot():
    seaborn.set(style="ticks", context="talk")

    tips = seaborn.load_dataset("tips")

    # Make a custom sequential palette using the cubehelix system
    pal = seaborn.cubehelix_palette(4, 1.5, .75, light=.6, dark=.2)

    # Plot tip as a function of toal bill across days
    grid = seaborn.lmplot(x="total_bill", y="tip", hue="day", data=tips, palette=pal, size=7)

    # Use more informative axis labels than are provided by default
    grid.set_axis_labels("Total bill ($)", "Tip ($)")

def scatter_plot_marginal_ticks():
    seaborn.set(style="white", color_codes=True)

    # Generate a random bivariate dataset
    sample = numpy.random.RandomState(9)
    mean = [0, 0]
    cov = [(1, 0), (0, 2)]
    x, y = sample.multivariate_normal(mean, cov, 100).T

    # Use JointGrid directly to draw a custom plot
    grid = seaborn.JointGrid(x, y, space=0, size=6, ratio=50)
    grid.plot_joint(pyplot.scatter, color="g")
    grid.plot_marginals(seaborn.rugplot, height=1, color="g")

def correlation_diagonal_matrix_heat_map():
    seaborn.set(style="white")
    sample = numpy.random.RandomState(33)
    density = pandas.DataFrame(data=sample.normal(size=(100, 26)), columns=list(ascii_uppercase))

    corr = density.corr()

    mask = numpy.zeros_like(corr, dtype=numpy.bool)
    mask[numpy.triu_indices_from(mask)] = True
    _, axis = pyplot.subplots(figsize=(11, 9))

    cmap = seaborn.diverging_palette(220, 10, as_cmap=True)
    seaborn.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, square=True, xticklabels=5, yticklabels=5, linewidths=.5, cbar_kws={"shrink": .5}, ax=axis)

def correlation_matrix_heat_map():
    seaborn.set(context="paper", font="monospace")

    data_frame = seaborn.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)
    corrmat = data_frame.corr()

    frame, axis = pyplot.subplots(figsize=(12, 9))

    seaborn.heatmap(corrmat, vmax=.8, square=True)

    # Use matplotlib directly to emphasize known networks
    networks = corrmat.columns.get_level_values("network")
    for i, network in enumerate(networks):
        if i and network != networks[i - 1]:
            axis.axhline(len(networks) - i, c="w")
            axis.axvline(i, c="w")

    frame.tight_layout()

def timeseries_plot():
    seaborn.set(style="darkgrid")
    gammas = seaborn.load_dataset("gammas")
    seaborn.tsplot(data=gammas, time="timepoint", unit="subject", condition="ROI", value="BOLD signal")

def time_series_bootstrap_resampling():
    seaborn.set(style="darkgrid", palette="Set2")

    sines = []
    rs = numpy.random.RandomState(8)
    for _ in range(15):
        x = numpy.linspace(0, 30 / 2, 30)
        y = numpy.sin(x) + rs.normal(0, 1.5) + rs.normal(0, .3, 30)
        sines.append(y)

    # Plot the average over replicates with bootstrap resamples
    seaborn.tsplot(sines, err_style="boot_traces", n_boot=500)

def category_scatter_plot():
    seaborn.set(style="whitegrid", palette="muted")
    iris = seaborn.load_dataset("iris")
    iris = pandas.melt(iris, "species", var_name="measurement")
    seaborn.swarmplot(x="measurement", y="value", hue="species", data=iris)

def horizontal_bar_plot():
    seaborn.set(style="whitegrid")

    # Initialize the matplotlib figure
    _, axis = pyplot.subplots(figsize=(6, 15))

    # Load the example car crash dataset
    crashes = seaborn.load_dataset("car_crashes").sort_values("total", ascending=False)

    # Plot the total crashes
    seaborn.set_color_codes("pastel")
    seaborn.barplot(x="total", y="abbrev", data=crashes, label="Total", color="b")

    # Plot the crashes where alcohol was involved
    seaborn.set_color_codes("muted")
    seaborn.barplot(x="alcohol", y="abbrev", data=crashes, label="Alcohol-involved", color="b")

    # Add a legend and informative axis label
    axis.legend(ncol=2, loc="lower right", frameon=True)
    axis.set(xlim=(0, 24), ylabel="", xlabel="Automobile collisions per billion miles")
    seaborn.despine(left=True, bottom=True)

def residual_plot():
    seaborn.set(style="whitegrid")
    sample = numpy.random.RandomState(7)
    x = sample.normal(2, 1, 75)
    y = 2 + 1.5 * x + sample.normal(0, 2, 75)
    seaborn.residplot(x, y, lowess=True, color="g")

def linera_regression_marginal_distributions_plot():
    seaborn.set(style="darkgrid", color_codes=True)
    tips = seaborn.load_dataset("tips")
    seaborn.jointplot("total_bill", "tip", data=tips, kind="reg", xlim=(0, 60), ylim=(0, 12), color="r", size=7)

def faceted_logistic_regression_plot():
    seaborn.set(style="darkgrid")
    data_frame = seaborn.load_dataset("titanic")
    palette = dict(male="#6495ED", female="#F08080")
    grid = seaborn.lmplot(x="age", y="survived", col="sex", hue="sex", data=data_frame, palette=palette, y_jitter=.02, logistic=True)
    grid.set(xlim=(0, 80), ylim=(-.05, 1.05))
