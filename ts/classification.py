import numpy as np
from constants import *


def addClassificationLabel(data):
    data['Label'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
    data = data.dropna()
    return data


def getColsToClassify(data, list):
    return data.loc[:, list]


def getColsToLabel(data):
    return data.loc[:, 'Label']


def getTrainTest(X, y):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    return x_train, x_test, y_train, y_test


def getScaledData(x_train, x_test):
    sc = StandardScaler()
    X_train = sc.fit_transform(x_train)
    X_test = sc.transform(x_test)
    return X_train, X_test


def getInputAlgorithms(data):
    X = getColsToClassify(data=data, list=data.columns[:5].tolist())
    y = getColsToLabel(data=data)
    x_train, x_test, y_train, y_test = getTrainTest(X=X, y=y)
    X_train, X_test = getScaledData(x_train=x_train, x_test=x_test)
    return X_train, X_test, y_train, y_test


def getPredictions(data, algorithm, algDict):
    X_train, X_test, y_train, y_test = getInputAlgorithms(data)
    classifier = algDict[algorithm]
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    return y_pred


def addClassifyPrediction(data, algorithms, algDict):
    for algorithm in algorithms:
        y_pred = getPredictions(data, algorithm, algDict)
        data.loc[-len(y_pred):, algorithm] = y_pred
    return data
