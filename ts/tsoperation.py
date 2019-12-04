from ts.read import getData
from ts.add_indicator import add_indicator
from ts.classification import *
from ts.RNN_Model_Save_Unique_Stock import *
import tensorflow as tf

stock = 'AKBNK'
timeframe = 'D'
df = getData(stock=stock, timeframe=timeframe)
df = add_indicator(data=df)
df = df.dropna()

RNNsave = 0
if RNNsave:
    stocksave = 'AKBNK'
    trainModel(main_df=df, RATIO_TO_PREDICT=stocksave)

RNNPredict = 1
indicatorsForTraining = ['HBTRENDMODE',
                         'TSF',
                         'CDLRISEFALL3METHODS']
columns = ['Close',
           'High',
           'Low',
           'Open',
           'Volume'] + indicatorsForTraining

if RNNPredict:
    stockpredict = 'AKBNK'
    modelSequenceLength = 10
    path = '/home/cem/PycharmProjects/untitled/{}-{}-backtest-MODE-{}-SEQ-2-PRED'.format(
        timeframe, stockpredict, modelSequenceLength)
    model = tf.keras.models.load_model('{}'.format(path))
    arrayForPredict = np.zeros((1, modelSequenceLength, 8))
    df = df[columns]
    # for i in range(30):
    #     x = df.iloc[-modelSequenceLength-i:-i,:]
    #     arrayForPredict[0] = x
    #     predict_matrix = model.predict(arrayForPredict)
    #     prediction = np.argmax(predict_matrix)
    #     print(prediction)
    x = df.iloc[-modelSequenceLength:]
    arrayForPredict[0] = x
    predict_matrix = model.predict(arrayForPredict)
    prediction = np.argmax(predict_matrix)



df = addClassificationLabel(data=df)
df = addClassifyPrediction(data=df,
                           algorithms=['logr',
                                       'knn',
                                       'svc_poly',
                                       'svc_linear',
                                       'svc_sigmoid',
                                       'gnb',
                                       'dtc',
                                       'rfc'])

df = addRegressionPrediction(data=df,
                             algorithms=['rf_reg', 'r_dt',
                                         'lin_reg',
                                         'svr_reg',
                                         # 'poly_reg'
                                         ],
                             dependentvariable='Close',
                             independentvariables=['High', 'Low', 'Open'])

df.to_excel('/home/cem/PycharmProjects/untitled/ts/{}-{}.xls'.format(stock, 'D'))
