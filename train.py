import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from sklearn.metrics import classification_report,accuracy_score, confusion_matrix
import seaborn as sns
from joblib import dump

file_name = 'part-088'
data = pd.read_csv('data/'+file_name+'.csv')
print("Data Ini")
print(data.head())
print(data.shape)

target = data["isAnomaly"]
print("Target")
print(target.head())
print("isAnomaly")
print(data['isAnomaly'].value_counts())

# Se eliminan columnas con datos iguales
def remove_constant_value_features(df):
    return [e for e in df if df[e].nunique() == 1]
data = data.drop(columns=remove_constant_value_features(data))
print("Constant Values Removed Column")
print(data.head())
print(data.shape)
np.sum(np.sum(data.isna()))

ori_data = data.copy()
#Se elimina la columna tiempo ya que no es relevante
data = data.drop(columns=['timestamp'])

# Se eliminan columnas no relevantes
rnd_clf = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
rnd_clf.fit(data, target)

not_imp = []
for name, importance in zip(data.columns, rnd_clf.feature_importances_):
    if importance > 0.020:
        not_imp.append(name)
print("Not Imp Column")
data = data.drop(columns=not_imp)
ori_data = ori_data.drop(columns=not_imp)

print(data.shape)

list_of_tuples = list(zip(data.columns, rnd_clf.feature_importances_))
pd.DataFrame(list_of_tuples, columns=['Columns', 'Importance']).sort_values(by='Importance', ascending=False)

cor_matrix = data.corr()
upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.95)]
data = data.drop(columns=to_drop)
ori_data = ori_data.drop(columns=to_drop)
print("ToDrop Column")
print(data.shape)
print(ori_data.shape)
ori_data.to_csv('data/test-'+file_name+'.csv')

print("Columns")
print(ori_data.columns)

factor = 1723/38797

clf = IsolationForest(n_estimators=100, max_samples=len(data), contamination=factor, random_state=0, verbose=0)
clf.fit(data)

dump(clf, 'models/isolation_forest.joblib')