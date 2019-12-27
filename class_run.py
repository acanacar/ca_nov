from ts_class import *

d = tstable(stock='GARAN.IS')
d.add_indicator()
d.classify('knn')

with pd.ExcelWriter(r'C:\Users\a.acar\PycharmProjects\ca_nov\outputs\ak.xlsx') as writer:
    d.classification_df.to_excel(writer,sheet_name='GARAN')

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

from sqlalchemy import create_engine
