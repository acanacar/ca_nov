import pandas as pd
import os
os.chdir('/media/goktug/Elements/DATABI/SIRKETLER')

#Butun Firmalarin Mali Tablolarini Okut

for f in os.listdir():
    xls = pd.ExcelFile(f)
    df1 = pd.read_excel(xls, 'Bilanço')
    df2 = pd.read_excel(xls, 'Gelir Tablosu')
    df3 = pd.read_excel(xls, 'Nakit Akım Tablosu')

    df1.fillna(0, inplace=True)
    df2.fillna(0, inplace=True)
    df3.fillna(0, inplace=True)

    df1['Kalem'] = df1['Kalem'].astype(str)

    df1.Kalem = df1.Kalem.astype(str)

    df1.set_index('Kalem', inplace=True)

    df2.set_index('Kalem', inplace=True)

    #Toplam Borclari hesaplamaca
    new_row = df1.loc['Kısa Vadeli Yükümlülükler'] + df1.loc['Uzun Vadeli Yükümlülükler']
    new_row.name = 'Toplam Yukumlulukler'
    df1 = df1.append([new_row])
    #Oranlari hesaplatmaca
    carior = df1.loc['Dönen Varlıklar'] / df1.loc['Kısa Vadeli Yükümlülükler']
    a = df1.loc['Dönen Varlıklar'] - df1.loc['Stoklar']
    lior = a/df1.loc['Kısa Vadeli Yükümlülükler']
    boovor = df1.loc['Toplam Yukumlulukler'] / df1.loc['Özkaynaklar']
    atr = df2.loc['Satış Gelirleri'] / df1.loc['TOPLAM KAYNAKLAR']
    grmar = 1-(df2.loc['Satışların Maliyeti (-)'] / df2.loc['Satış Gelirleri'])
    roa = df1.loc['Dönem Net Kar/Zararı'] / df1.loc['TOPLAM KAYNAKLAR']
    roe = df1.loc['Dönem Net Kar/Zararı'] / df1.loc['Özkaynaklar']
    ros= df1.loc['Dönem Net Kar/Zararı'] / df2.loc['Satış Gelirleri']
    data = [carior, lior, boovor, atr, grmar, roa, roe, ros]
    baslik = ['2019/9', '2019/6', '2019/3', '2018/12',
          '2018/9',	'2018/6', '2018/3', '2017/12',
          '2017/9',	'2017/6', '2017/3', '2016/12', '2016/9',
          '2016/6']
    ndx = ['carior', 'lior', 'boovor', 'atr', 'grmar', 'roa', 'roe', 'ros']
    #hesaplanan oranlardan yeni dataframe yapmak

    ratios = pd.DataFrame(data, index=ndx, columns=baslik).transpose()

    ratios['firma'] = f[:5]
    ad = f[:5] + '.csv'
    ratios = ratios.iloc[::-1]
    ratios.to_csv('/media/goktug/Elements/DATABI/ORAN/{}'.format(ad))





















