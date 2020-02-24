from ts_table.variables import *
import pandas as pd
from trash.ts.add_indicator import *
from trash.ts.classification import getScaledData

data = pd.read_pickle(hist_pkl)

all_securities = data.columns.get_level_values(0).unique()

#
securities = ['AKBNK.IS']
data = data.loc[:, (securities, slice(None))]
data.columns = data.columns.droplevel(0)
data = data.dropna(axis=1, how='all').dropna(axis=0, how='any')
#
df_indicator = add_indicator(data_frame=data)

#
df_classification = data.copy()
df_classification['return'] = data['Adj Close'].pct_change()


def conditions(r, yuzde_1=False):
    if yuzde_1 is False:
        if r['return'] > 0:
            return 1
        elif r['return'] == 0:
            return 0
        else:
            return -1
    else:
        if r['return'] >= 0.01:
            return 1
        elif r['return'] <= -0.01:
            return -1
        else:
            return 0


df_classification['label'] = df_classification.apply(conditions, yuzde_1=False, axis=1)
df_classification['label_yuzdeBir'] = df_classification.apply(conditions, yuzde_1=True, axis=1)
df_classification = df_classification.iloc[1:]

algorithms = ['logr', 'knn', 'svc_poly', 'svc_linear',
              'svc_sigmoid', 'gnb', 'dtc', 'rfc']
for algorithm in algorithms:
    classifier = algDict[algorithm]

    labelcol = 'label'
    cols_to_classify = ['Close', 'High', 'Low', 'Open', 'Volume']
    X = df_classification.loc[:, cols_to_classify]
    Y = df_classification.loc[:, labelcol]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    x_train, x_test = getScaledData(x_train, x_test)

    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    df_classification.loc[-len(y_pred):, algorithm] = y_pred

#
df_regression = data.copy()
df_regression['return'] = data['Adj Close'].pct_change()


#



