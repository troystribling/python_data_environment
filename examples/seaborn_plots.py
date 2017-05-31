import numpy as np
import matplotlib.pyplot as pyplot
import pandas
import seaborn

def line_plots():
    seaborn.set(style="ticks")
    df = seaborn.load_dataset("anscombe")
    seaborn.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
                   col_wrap=2, ci=None, palette="muted", size=4, scatter_kws={"s": 50, "alpha": 1})
def polar_plot():
    seaborn.set()
    r = np.linspace(0, 10, num=100)
    df = pandas.DataFrame({'r': r, 'slow': r, 'medium': 2 * r, 'fast': 4 * r})
    df = pandas.melt(df, id_vars=['r'], var_name='speed', value_name='theta')
    g = seaborn.FacetGrid(df, col="speed", hue="speed", subplot_kws=dict(projection='polar'), size=4.5, sharex=False, sharey=False, despine=False)
    g.map(pyplot.scatter, "theta", "r")
