# %%
%reload_ext autoreload
%autoreload 2
%aimport sys, os
local_lib_path = os.getcwd() + '/examples'
if local_lib_path not in sys.path:
    sys.path.append(local_lib_path)
import seaborn_plots

# %%
seaborn_plots.line_plots()
# seaborn_plots.line_plots()
