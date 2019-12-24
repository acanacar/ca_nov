from ts_class import *

d = tstable(stock='AKBNK.IS')
d.add_indicator()
d.classify('knn')


df = pd.read_pickle(hist_pkl)

tahvils = ['tahvil2y', 'tahvil5y', 'tahvil10y']

for tahvil in tahvils:
    path = str(data_path / '{}.csv'.format(tahvil))
    dframe = pd.read_csv(path, sep=';', decimal=',')
    dframe['Date'] = pd.to_datetime(dframe['Date'])
    dframe.set_index('Date', inplace=True)
    dframe.to_hdf(hdf5_store,
                  key='daily/{}'.format(tahvil),
                  mode='w',
                  format='table')
    # df[tahvil] = dframe

store = pd.HDFStore(hdf5_store)