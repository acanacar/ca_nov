import yfinance as yf
from constants import *

# Bist30 1min,60min and daily download and store
tickers = Tickers()

# df = yf.download(' '.join(tickers), '2019-12-02', '2019-12-03', group_by='ticker', interval='1m')
# df.to_pickle(hist_pkl_1m)
df = pd.read_pickle(hist_pkl_1m)
df.to_hdf(hdf5_store, key='minute/tickers', mode='w', format='table')

# df = yf.download(' '.join(tickers), '2018-01-01', '2019-12-01', group_by='ticker', interval='60m')
# df.to_pickle(hist_pkl_1h)
df = pd.read_pickle(hist_pkl_1h)
df.to_hdf(hdf5_store, key='hour/tickers', format='table')

# df = yf.download(' '.join(tickers), '2015-01-01', '2019-12-01', group_by='ticker')
# df.to_pickle(hist_pkl)
df = pd.read_pickle(hist_pkl)
df.to_hdf(hdf5_store, key='daily/tickers', format='table')

vix_tickers = ['VXX', 'UVXY', 'SVXY']
df_vix = yf.download(' '.join(vix_tickers), '2015-01-01', '2019-12-01', group_by='ticker')
df_vix.to_hdf(hdf5_store, key='daily/vix', format='table')

# 'BZ=F' icin historic son 20 gun var
# GC=F icin son 1 yil var
# '^VIX' icin son 1 yil var
vix_tickers_v2 = ['BZ=F', 'GC=F', '^VIX']
df_vix_v2 = yf.download(' '.join(vix_tickers_v2), '2015-01-01', '2019-12-01', group_by='ticker')
df_vix_v2.to_hdf(hdf5_store, key='daily/vix_v2', format='table')

US_BONDS = ['^FVX', '^TNX']
df_usbonds = yf.download(' '.join(US_BONDS), '2015-01-01', '2019-12-01', group_by='ticker')
df_usbonds.to_hdf(hdf5_store, key='daily/usbonds', format='table')




df_tahvils = pd.read_pickle(tahvil_pkl)
df_tahvils.to_hdf(hdf5_store, key='daily/tahvils', format='table')

df_ = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
df_.to_hdf(hdf5_store, key='daily/df_', format='table')

df_x = pd.DataFrame({'A': [9], 'B': [7]}, index=['d'])

store = pd.HDFStore(hdf5_store)
store.append(key='daily/df_', value=df_x, format='table')
store.append(key='daily/df_', value=df_, format='table')
store.append(key='daily/df_', value=df_.iloc[[-1]], format='table')
store.close()
