import sys, os
local_lib_path = os.getcwd() + '/examples'
if local_lib_path not in sys.path:
    sys.path.append(local_lib_path)
import simple_plots

simple_plots.line_plot()
