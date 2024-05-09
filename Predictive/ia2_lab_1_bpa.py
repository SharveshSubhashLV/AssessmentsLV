# -*- coding: utf-8 -*-
"""IA2-LAB-1-BPA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1utAr6rdSIgfRrpjiFEvRfTd18ex6YQ8s
"""

import pandas as pd
df = pd.read_csv("/content/winequality-red.csv")
df.head()

df.describe()

"""**Cleaning Data, removing null values and duplicates**"""

df.isna().sum()

"""only around 1-2% of each column has null values, so those can be filled with mean value."""

df['fixed acidity'].fillna(df['fixed acidity'].mean(), inplace=True)
df['volatile acidity'].fillna(df['volatile acidity'].mean(), inplace=True)
df['citric acid'].fillna(df['citric acid'].mean(), inplace=True)
df['residual sugar'].fillna(df['residual sugar'].mean(), inplace=True)
df['chlorides'].fillna(df['chlorides'].mean(), inplace=True)
df['free sulfur dioxide'].fillna(df['free sulfur dioxide'].mean(), inplace=True)
df['sulphates'].fillna(df['sulphates'].mean(), inplace=True)
df

df.info()

df = df.drop_duplicates()

df.info()

"""**Identifying outliers**"""

import seaborn as s
s.boxplot(df['free sulfur dioxide'])

df= df[df['free sulfur dioxide']<42]
df

s.boxplot(df['chlorides'])

df = df[df['chlorides']<0.12]
df

s.boxplot(df['fixed acidity'])

df = df[df['fixed acidity']<12.2]
df

s.boxplot(df['volatile acidity'])

df = df[df['volatile acidity']<1.0]
df

s.boxplot(df['citric acid'])

df = df[df['citric acid']<0.8]
df

s.boxplot(df['residual sugar'])

df = df[df['residual sugar']<=3.7]
df

s.boxplot(df['sulphates'])

df = df[df['sulphates']<0.85]
df

s.boxplot(df['pH'])

df = df[df['pH']<3.62]
df=df[df['pH']>=3.0]
df

s.boxplot(df['alcohol'])

df = df[df['alcohol']<13]
df

"""**Removed All outliers**"""

df['quality'].mean()

df['quality'].min()

df['quality'].max()

df['quality_level']=["Bad" if x <=5.5 else "Good" for x in df['quality']]

df

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
df['quality_level'] = lb.fit_transform(df['quality_level'])
df

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

x_train, x_test, y_train, y_test = train_test_split(df.drop(['quality','quality_level'],axis='columns'),df['quality_level'],test_size=0.3)

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100, random_state=42)

clf.fit(x_train, y_train)
predictions = clf.predict(x_test)



accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", round(accuracy*100,2),"%")
prec = precision_score(y_test, predictions)
print("Precision:", round(prec*100,2),"%")
recall = recall_score(y_test, predictions)
print("Recall:", round(recall*100,2),"%")