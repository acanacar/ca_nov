'''
Sınıflama:
1. Sanayi ve Ticaret,
2- Banka,
3- Faktoring Leasing ,
4- Aracı Kurumlar,
5- G.Menkul Sermaye Şirketleri
6- Holdingler.
'''

import pandas as pd
from fintable.ratio_functions import *
from fintable.variables import *

stocks = [t for t, cat in mali_tablo_tickers if cat == 'sanayi']
# stocks = [t for t, cat in mali_tablo_tickers if cat == None]

tablos = ['Bilanço', 'Gelir Tablosu']

l = []
for stock in stocks:
    for tablo in tablos:
        path = mali_tablolar_path / Path(r'{} Finansal Tablolar.xlsx'.format(stock))
        # path = mali_tablolar_path / Path(r'{}_Finansal_Tablolar_Bilanco.xlsx'.format(stock))
        df = pd.read_excel(open(str(path), 'rb'), sheet_name=tablo)
        df['tablo'], df['stock'] = [tablo, stock]
        l.append(df)

df = pd.concat(l, ignore_index=True, join='inner')

a = []
for col in df.columns[1:-2]:
    dfx = df[['Kalem', 'stock', col]].copy()
    dfx['period'] = col
    dfx.columns = ['Kalem', 'stock', 'value', 'period']
    a.append(dfx)

df2 = pd.concat(a, ignore_index=True, join='inner')
df2.set_index(['stock', 'period', 'Kalem'], inplace=True)
df2.sort_index(inplace=True)

# df2.loc[('AKBNK', '2018/3', 'CARİ VERGİ BORCU'), ['value']].values[0][0]
# df2.loc[('AKBNK', '2018/3', (slice(None))), ['value']]

r = [
    'bovor',  # bovor
    'enterpriseValue',  # enterprise_value
    'akdor',  # akdor
    'ebit',  # ebit
    'ebitda',  # ebitda
    'EBITDA_MARGIN',  # ebitdam
    'EPS_Growth',  # eps_growth
    'Gross_Margin',  # gross_margin
    'Net_Margin',  # net_margin
    'Interest_Burden'  # interest_burden
    'bdor',  # bdor
    'Net_Income_Growth',  # net_income_growth
    'Pay_Out_Ratio',  # pay_out_ratio
    'RoAs',  # roas
    'RoEq',  # roeq
    'RoSa',  # rosa
    'Current_Ratio',  # current_ratio
    'Acid_Test_Ratio',  # acid_test_ratio
    'Price_to_Book_value',  # price_to_book_ratio
    'Market_cap',  # market_cap
    'Price_Earning_Ratio',  # price_earning_ratio
    'Enterprise_value_over_EBIT',  # enterprise_value_over_ebit
    'Enterprise_value_over_EBITDA'  #
]

my_index = pd.MultiIndex(levels=[df2.index.levels[0], df2.index.levels[1], r],
                         codes=[[], [], []],
                         names=df2.index.names)
my_columns = ['value']
df3 = pd.DataFrame(index=my_index, columns=my_columns)

donems = ['2019/3',
          '2018/12', '2018/9', '2018/6', '2018/3',
          '2017/12', '2017/9', '2017/6', '2017/3',
          '2016/12', '2016/9', '2016/6'
          ]

ratio_dict = {
    'sanayi':
        {'dkar': 'Dönem Net Kar/Zararı',
         'dvg': 'Dönem Vergi (Gideri) Geliri',  # yanlis
         'dv': 'Dönen Varlıklar',
         'tv': 'Özkaynaklar',
         'to': 'Özkaynaklar',
         'fgid': 'Finansman Giderleri',  #
         'fgel': 'Finansman Gelirleri',
         # 'nfg': 'NET FAİZ GELİRİ VEYA GİDERİ',
         'kvb': 'Kısa Vadeli Yükümlülükler',
         'uvb': 'Uzun Vadeli Yükümlülükler',
         'stok': 'Stoklar',
         'sg': 'Satış Gelirleri',
         'tk': 'TOPLAM KAYNAKLAR',
         'sm': 'Satışların Maliyeti (-)'

         }}

# df3.loc[('AKBNK', '2018/3', 'Market_cap'), ['value']]=1
for stock in stocks[:]:
    print(stock)
    for period in df2.index.levels[1]:
        keys = ratio_dict['sanayi']
        dkar = df2.loc[(stock, period, keys['dkar']), ['value']].values[0][0]
        # donem kari
        # dvg = df2.loc[(stock, period, 'Dönem Vergi (Gideri) Geliri'), ['value']].values[0][0]
        # donem vergisi gideri geliri  --> Dönem Vergi (Gideri) Geliri yanlis
        # evg
        # ertelenmis vergi gideri geliri
        tv = df2.loc[(stock, period, keys['tv']), ['value']].values[0][0]
        # toplam varlik,
        to = df2.loc[(stock, period, keys['to']), ['value']].values[0][0]
        # toplam ozkaynak
        # hasilat
        # net ciro
        # fgid = df2.loc[(stock, period, 'Finansman Giderleri'), ['value']].values[0][0]
        # finansman giderleri  --> Finansman Giderleri yanlis
        # fgel = df2.loc[(stock, period, 'Finansman Gelirleri'), ['value']].values[0][0]
        # finansman gelirleri  --> Finansman Gelirleri yanlis
        # amortisman
        # Amortisman ve İtfa Gideri İle İlgili Düzeltmeler
        # smm
        # Satılan Malın Maliyeti
        # nfg = df2.loc[(stock, period, keys['nfg']), ['value']].values[0][0]
        # net faiz geliri
        # odkar
        # Bir Önceki Dönem Karı
        # dd
        # donen degerler
        kvb = df2.loc[(stock, period, keys['kvb']), ['value']].values[0][0]
        # kisa vadeli borclar
        uvb = df2.loc[(stock, period, keys['uvb']), ['value']].values[0][0]
        # uzun vadeli borclar
        ty = kvb + uvb
        # toplam yukumluluk
        dv = df2.loc[(stock, period, keys['dv']), ['value']].values[0][0]
        stok = df2.loc[(stock, period, keys['stok']), ['value']].values[0][0]
        # stoklar
        sg = df2.loc[(stock, period, keys['sg']), ['value']].values[0][0]
        # Satış Gelirleri
        tk = df2.loc[(stock, period, keys['tk']), ['value']].values[0][0]
        # TOPLAM KAYNAKLAR
        sm = df2.loc[(stock, period, keys['sm']), ['value']].values[0][0]

        df3.loc[(stock, period, 'carior')] = carior(dv=dv, kvb=kvb)
        df3.loc[(stock, period, 'lior')] = lior(dv=dv, stok=stok, kvb=kvb)
        df3.loc[(stock, period, 'boovor')] = boovor(ty=ty, to=to)
        df3.loc[(stock, period, 'atr')] = atr(sg=sg, tk=tk)
        df3.loc[(stock, period, 'grmar')] = grmar(sm=sm, sg=sg)
        df3.loc[(stock, period, 'roa')] = roa(dkar=dkar, tk=tk)
        df3.loc[(stock, period, 'RoEq')] = roeq(dkar, to)
        df3.loc[(stock, period, 'RoS')] = rosa(dkar=dkar, sg=sg)

        # df3.loc[(stock, period, 'enterpriseValue')]=enterprise_value()
        # df3.loc[(stock, period, 'akdor')]=akdor(hasilat,tv)
        # df3.loc[(stock, period, 'ebit')]=ebit(dkar, dvg, evg, fgid, fgel)
        # df3.loc[(stock, period, 'ebitda')]=ebitda(ebit, amortisman)
        # df3.loc[(stock, period, 'EBITDA_MARGIN')]=ebitdam(ebitda, hasilat)
        # df3.loc[(stock, period, 'EPS_Growth')]=eps_growth()
        # df3.loc[(stock, period, 'Gross_Margin')]=gross_margin(smm, has)
        # df3.loc[(stock, period, 'Net_Margin')]=net_margin(dkar, has)
        # df3.loc[(stock, period, 'Interest_Burden')]=interest_burden(dkar, dvg, evg, ebit)
        # df3.loc[(stock, period, 'bdor')]=bdor(ebit, nfg)
        # df3.loc[(stock, period, 'Net_Income_Growth')]=net_income_growth(dkar, odkar)
        # df3.loc[(stock, period, 'Pay_Out_Ratio')]=pay_out_ratio()
        # df3.loc[(stock, period, 'RoAs')] = roas(dkar, tv)
        # df3.loc[(stock, period, 'RoEq')] = roeq(dkar, to)
        # df3.loc[(stock, period, 'RoSa')]=rosa(dkar, has)
        # df3.loc[(stock, period, 'Current_Ratio')]=current_ratio(dd, kvb)
        # df3.loc[(stock, period, 'Acid_Test_Ratio')]=acid_test_ratio(dd, stok, kvb)
        # df3.loc[(stock, period, 'Price_to_Book_value')]=price_to_book_ratio()
        # df3.loc[(stock, period, 'Market_cap')]=market_cap()
        # df3.loc[(stock, period, 'Price_Earning_Ratio')]=price_earning_ratio()
        # df3.loc[(stock, period, 'Enterprise_value_over_EBIT')]=enterprise_value_over_ebit()
        # df3.loc[(stock, period, 'Enterprise_value_over_EBITDA')]=#
