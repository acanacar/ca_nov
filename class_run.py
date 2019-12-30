from ts_class import *

stock_name = 'GARAN.IS'

d = tstable(stock=stock_name)
d.add_indicator()
d.classify('knn')
d.regression('lin_reg')
d.to_excel()
df = pd.read_pickle(hist_pkl)

tahvils = ['tahvil2y', 'tahvil5y', 'tahvil10y']

tahvil_dfs = []
for tahvil in tahvils:
    path = str(data_path / '{}.csv'.format(tahvil))
    dframe = pd.read_csv(path, sep=';', decimal=',')
    dframe['Date'] = pd.to_datetime(dframe['Date'])
    dframe.set_index('Date', inplace=True)
    dframe['stock'] = tahvil
    tahvil_dfs.append(dframe)
    # dframe.to_hdf(hdf5_store,
    #               key='daily/{}'.format(tahvil),
    #               mode='w',
    #               format='table')
    # df[tahvil] = dframe

data = pd.concat(tahvil_dfs, axis=0)

store = pd.HDFStore(hdf5_store)

