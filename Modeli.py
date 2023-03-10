# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jB7RFWclG1PLp2xk1LCP8InrbcRqzlJ4
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import warnings 
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import GridSearchCV,cross_val_score
import pickle
import os
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.metrics import f1_score, precision_score, recall_score,accuracy_score
import joblib


for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df=pd.read_csv("/content/diabetes.csv")

df.head(6) 
df.describe()
df.isnull().sum()

df.hist(bins=10,figsize=(10,10))
plt.show()

target_name='Outcome'
y= df[target_name]
X=df.drop(target_name,axis=1)
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X =  pd.DataFrame(sc_X.fit_transform(df.drop(["Outcome"],axis = 1),),
        columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'])


X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2,stratify=y,random_state=0)
#print(X_train.shape)
#print(X_test.shape)

k_values = range(1, 31)


cv_scores = []
for k in k_values:
    scores = cross_val_score(knn_model, X_train, y_train, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())

best_k = k_values[cv_scores.index(max(cv_scores))]

#K-nearest neighbors
#knn_model = KNeighborsClassifier(n_neighbors = best_k)
#knn_model.fit(X_train, y_train)
#pickle.dump(knn_model, open('knn_model.pkl','wb')) 
#X_train_prediction = knn_model.predict(X_train)
#training_data_accuracy = accuracy_score(X_train_prediction, y_train)
#print('Accuracy on Training data for K-Nearest Neighbour: ', training_data_accuracy)
#X_test_prediction = knn_model.predict(X_test)
#test_data_accuracy = accuracy_score(X_test_prediction, y_test)
#print('Accuracy on Test data for K-Nearest Neighbour: ', test_data_accuracy)
#print()
#print("Confusion matrix: ")
#confusion_matrix = confusion_matrix(y_test, X_test_prediction)
#print(confusion_matrix)
#print("Classification report: ")
#report = classification_report(y_test, X_test_prediction)
#print(report)



#LogisticRegression
#lr_model = LogisticRegression(max_iter = 3000)
#lr_model.fit(X_train, y_train)
#pickle.dump(lr_model, open('lr_model.pkl','wb')) 
#X_train_prediction = lr_model.predict(X_train)
#training_data_accuracy = accuracy_score(X_train_prediction, y_train)
#print('Accuracy on Training data for Logistic Regression: ', training_data_accuracy)
#X_test_prediction = lr_model.predict(X_test)
#test_data_accuracy = accuracy_score(X_test_prediction, y_test)
#print('Accuracy on Test data for Logistic Regression: ', test_data_accuracy)
#print()
#print("Confusion matrix: ")
#confusion_matrix = confusion_matrix(y_test, X_test_prediction)
#print(confusion_matrix)
#print("Classification report: ")
#report = classification_report(y_test, X_test_prediction)
#print(report)

#SVM

model = SVC()
kernel = ['poly', 'rbf', 'sigmoid']
C = [50, 10, 1.0, 0.1, 0.01]
gamma = ['scale']
#define grid_search
grid = dict(kernel=kernel,C=C,gamma=gamma)
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
grid_search = GridSearchCV(estimator=model, param_grid=grid, n_jobs=-1, cv=cv, scoring='f1',error_score=0)
grid_result = grid_search.fit(X, y)
svm_pred=grid_result.predict(X_test)
print("Classification Report is:\n",classification_report(y_test,svm_pred))
#print("\n F1:\n",f1_score(y_test,knn_pred))
#print("\n Precision score is:\n",precision_score(y_test,knn_pred))
#print("\n Recall score is:\n",recall_score(y_test,knn_pred))
print("\n Confusion Matrix:\n")
print("Confusion matrix: ")
confusion_matrix = confusion_matrix(y_test,svm_pred )
print(confusion_matrix)
print()