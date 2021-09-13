import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from sklearn.metrics import classification_report,accuracy_score, confusion_matrix
import seaborn as sns
from joblib import load

clf = load("models/isolation_forest.joblib")
csv_data = pd.read_csv("data/test.csv", index_col=0).to_numpy()

for info in csv_data:
    test_data = np.delete(info, 0)
    #print(test_data)

    #test_data = [0.9713541666666666,63177936.0,0.0,65.0,0.0,0.0,0.3401080289297812,0.8009054349816364,0.0,0.0,0.825,1056768.0,0.0,0.8440896739130435,71.0,0.0,0.9953984837074064,1102300000000.0,0.0,0.1511822594329714,0.0,0.0,73.0,0.0,0.0742378721669611,1.2953586497890297,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,40.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.1463424569464947,0.0,0.0,0.0,0.0,0.0,0.016417350841546,0.0,0.369384765625,0.0,0.0,0.145263671875,1026.0,0.0,0.0]
    data = np.array(test_data).reshape(1, -1)

    #print("Data")
    #print(data)

    prediction = clf.predict(data)
    if prediction == -1:
        print("prediction")
        print(prediction)

        score = clf.score_samples(data)
        print("score")
        print(score)

        roundes_score = np.round(score, 3).tolist()
        print("roundes_score")
        print(roundes_score)

        print("Data")
        print(info[0])






