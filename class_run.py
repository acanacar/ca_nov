from ts_class import *

stock_name = 'GARAN.IS'
stock_name = 'XU100.IS'

# istenen stoga ait obje olusur
d = tstable(stock=stock_name)

# secilen stoga ait indicatorler dataframe e yeni kolon olarak eklenir.
d.add_indicator()

# secilen stoga ait secilen classification algoritmasi calistirilir ve self.classification_df olarak objeye kaydedilir.
d.classify('knn')
d.classify('svc_poly')
d.classify('logr')

# secilen stoga ait secilen regresyon algoritmasi calistirilir ve self.regression_df olarak objeye kaydedilir.
d.regression('lin_reg')

# bu komut ile indicatorleri iceren dataframe, regression sonuclarini iceren dataframe ve
# classification sonuclarini iceren dataframe excele farkli bir sheete (sheetname = stock adi olur) kaydedilir.
d.to_excel()


# butun ticker lara ait veriler (us bonds, tahvil, hisseler, altin,dolar vb.) excele farkli sheetler
# halinde aktarilir.
d.external_datas_to_excel()
# eldeki butun tickerlar icin korelasyon matrisi hesaplanir
d.calculate_correlation()
# korelasyon matrisinin excele farkli bir sheet olarak atilir.
d.correlation_to_excel()
# sentdex apiden cekilen sentiment veriler dataframe haline getirilir ve self.sentiment_df olarak objeye kaydedilir.
d.get_sentiment_df()
print(d.sentiment_df.head())


