# %%
%matplotlib inline
%reload_ext autoreload
%autoreload 2

import numpy
from scipy.stats import norm

from examples import stats_plots
from examples import bernoulli_trials

# %%
# Consider two independent Bernoulli trials with probability pa and pb and
# counts na and nb. Define a new random variable, pa = ha/na and pb = hb/nb. Where ha and hb
# are the number of heads for process a and b respectivelyt. Consider the difference of the
# prcocesses, namely p = pa - pb. The combined denisty will be fp = fpa*fpb.
# it follows that the mean of the combined process is μ = μa-μb = na*pa-nb*pb.
# The variance will be Var(x) = E(xa^2)+E(xb^2)-(na * pa)^2-(nb*pb)^2 = σa^2+σb^2 = pa*na*(1-pa)+pa*na*(1-pa).
