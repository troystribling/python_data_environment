%matplotlib inline
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn

def line_plots():
    seaborn.set(style="ticks")
    df = seaborn.load_dataset("anscombe")
    seaborn.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
                   col_wrap=2, ci=None, palette="muted", size=4, scatter_kws={"s": 50, "alpha": 1})

def histograms():
