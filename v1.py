from constants import *
import pandas as pd
from ts.add_indicator import *

data = pd.read_pickle(hist_pkl)

all_securities = data.columns.get_level_values(0).unique()

securities = ['AKBNK.IS']
data = data.loc[:, (securities, slice(None))]
data.columns = data.columns.droplevel(0)

df = add_indicator(data=data)
