import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix
import talib
import pickle


def addClassificationLabel(data):
    data['Label'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
    data = data.dropna()
    return data


def getColsToClassify(data, list):
    return data.loc[:, list]


def getColsToLabel(data):
    return data.loc[:, 'Label']


from sklearn.model_selection import train_test_split


def getTrainTest(X, y):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    return x_train, x_test, y_train, y_test


# verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler


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


# 1. Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

logr = LogisticRegression(random_state=0)
# 2. KNN
knn = KNeighborsClassifier(n_neighbors=1, metric='minkowski')
# 3. SVC (SVM classifier)
svc_poly = SVC(kernel='poly')
svc_linear = SVC(kernel='linear')
svc_sigmoid = SVC(kernel='sigmoid')
# 4. NAive Bayes
gnb = GaussianNB()
# 5. Decision tree
dtc = DecisionTreeClassifier(criterion='entropy')
# 6. Random Forest
rfc = RandomForestClassifier(n_estimators=10, criterion='entropy')

algDict = {'logr': logr,
           'knn': knn,
           'svc_poly': svc_poly,
           'svc_linear': svc_linear,
           'svc_sigmoid': svc_sigmoid,
           'gnb': gnb,
           'dtc': dtc,
           'rfc': rfc}


def getPredictions(data, algorithm):
    X_train, X_test, y_train, y_test = getInputAlgorithms(data)
    classifier = algDict[algorithm]
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    return y_pred


def addClassifyPrediction(data, algorithms):
    for algorithm in algorithms:
        y_pred = getPredictions(data, algorithm)
        data.loc[-len(y_pred):, algorithm] = y_pred
    return data
