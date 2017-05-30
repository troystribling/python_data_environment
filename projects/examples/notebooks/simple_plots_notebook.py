%load_ext autoreload
%autoreload 2
import sys, os, importlib
local_lib_path = os.getcwd() + '/examples'
if local_lib_path not in sys.path:
    sys.path.append(local_lib_path)
import simple_plots

# %%
simple_plots.line_plot()

# %%
simple_plots.bar_chart()

# %%
simple_plots.histogram()

# %%
simple_plots.multiple_line_charts()
