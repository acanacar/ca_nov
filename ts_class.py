from constants import *
from ts.add_indicator import *

import requests
import io


# res = requests.get('http://sentdex.com/api/finance/sentiment-signals/sample/')
# if res.status_code is 200:
#     response = res.content
#     # lines = response.splitlines()
#     sentiment_dataframe = pd.read_csv(io.StringIO(response.decode('utf-8')))
#     sentiment_dataframe['date'] = pd.to_datetime(sentiment_dataframe['date'])

class tstable(object):
    algDict = {'logr': logr,
               'knn': knn,
               'svc_poly': svc_poly,
               'svc_linear': svc_linear,
               'svc_sigmoid': svc_sigmoid,
               'gnb': gnb,
               'dtc': dtc,
               'rfc': rfc}
    data = pd.read_pickle(hist_pkl)

    def __init__(self, stock):
        self.stock = stock
        data = tstable.data.loc[:, ([self.stock], slice(None))]
        data.columns = data.columns.droplevel(0)
        self.dataframe = data.dropna(axis=1, how='all').dropna(axis=0, how='any')
        self.return_series = self.dataframe['Adj Close'].pct_change().iloc[1:]
        self.indicator_df = self.dataframe.iloc[1:]
        self.classification_df = self.dataframe.iloc[1:]
    
    def add_indicator(self):
        self.indicator_df = add_indicator(data_frame=self.indicator_df)

    def set_classification_label(self):

        def conditions_series(r, yuzde_1=False):
            if yuzde_1 is False:
                if r > 0:
                    return 1
                elif r == 0:
                    return 0
                else:
                    return -1
            else:
                if r >= 0.01:
                    return 1
                elif r <= -0.01:
                    return -1
                else:
                    return 0

        self.classification_df.loc[:, 'label'] = self.return_series.apply(conditions_series, yuzde_1=False)
        self.classification_df.loc[:, 'label_1_pct'] = self.return_series.apply(conditions_series,
                                                                                yuzde_1=True)

    def set_cols_to_classify(self, input_cols):
        self.classifying_input_cols = input_cols
        self.classify_input = self.classification_df.loc[:, self.classifying_input_cols]

    def getScaledData(self, x_train, x_test):
        sc = StandardScaler()
        self.x_train = sc.fit_transform(x_train)
        self.x_test = sc.transform(x_test)

    def set_train_test_data(self):
        X = self.classify_input
        Y = self.classification_df['label']
        x_train, x_test, self.y_train, self.y_test = train_test_split(X, Y,
                                                                      test_size=0.3, random_state=0)
        self.getScaledData(x_train, x_test)

    def set_classifier(self, algo='logr'):
        self.classifier = algDict[algo]

    def fit_classifier(self):
        self.classifier.fit(self.x_train, self.y_train)

    def make_predictions(self):
        self.y_predictions = self.classifier.predict(self.x_test)

    def set_predictions_to_dataframe(self, algo):
        self.classification_df.loc[-len(self.y_predictions):, algo] = self.y_predictions

    def classify(self, algo, input_cols=['Open', 'High', 'Low', 'Close', 'Volume']):
        self.set_cols_to_classify(input_cols=input_cols)
        self.set_classification_label()
        self.set_classifier(algo=algo)
        self.set_train_test_data()
        self.fit_classifier()
        self.make_predictions()
        self.set_predictions_to_dataframe(algo)
