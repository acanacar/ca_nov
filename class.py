from constants import *
from ts.add_indicator import *


class tstable(object):
    def __init__(self, stock):
        self.stock = stock

    def set_dataframe(self):
        data = pd.read_pickle(hist_pkl)
        data.columns = data.columns.droplevel(0)
        self.dataframe = data.dropna(axis=1, how='all').dropna(axis=0, how='any')
        self.indicator_df = self.dataframe
        self.classification_df = self.dataframe

    def add_indicator(self):
        self.indicator_df = add_indicator(data_frame=self.indicator_df)

    def set_classification(self):
        self.classification_df['return'] = self.classification_df['Adj Close'].pct_change()

    def set_classification_label(self):
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

        self.classification_df['label'] = self.classification_df.apply(conditions, yuzde_1=False, axis=1)
        self.classification_df['label_yuzdeBir'] = self.classification_df.apply(conditions, yuzde_1=True, axis=1)
        self.classification_df = self.classification_df.iloc[1:]

    def set_cols_to_classify(self, cols):
        self.cols_to_classify = cols
        self.classify_data = self.classification_df[:, self.cols_to_classify]

