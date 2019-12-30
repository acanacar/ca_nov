# korelasyon sutunu icin


from constants import *
import pandas as pd

data = pd.read_pickle(hist_pkl)

all_securities = data.columns.get_level_values(0).unique()

#
data.columns = data.columns.swaplevel(0, 1)
data = data.loc[:, (['Adj Close'], slice(None))]
data.columns = data.columns.droplevel(0)
data = data.dropna(axis=1, how='all').dropna(axis=0, how='any')

#
data = data.pct_change().iloc[1:]

cov_mat = data.cov()
cor_mat = data.corr()
