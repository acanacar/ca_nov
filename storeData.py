import yfinance as yf
from constants import *

tickers = Tickers()

df = yf.download(' '.join(tickers), '2019-12-02', '2019-12-03', group_by='ticker', interval='1m')
df.to_pickle(hist_pkl_1m)

df = yf.download(' '.join(tickers), '2018-01-01', '2019-12-01', group_by='ticker', interval='60m')
df.to_pickle(hist_pkl_1h)

df = yf.download(' '.join(tickers), '2015-01-01', '2019-12-01', group_by='ticker')
df.to_pickle(hist_pkl)
