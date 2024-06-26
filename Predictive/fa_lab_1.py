# -*- coding: utf-8 -*-
"""FA_Lab_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UY93M1_MkCzbV0B4RrDppYtlC-k8UpfS
"""

import pandas as pd
df = pd.read_csv("/content/prediction.csv")
df.info()

df.head()

df.describe()

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import xgboost as xgb
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

corr = df.corr(numeric_only= True)
sns.heatmap(corr,annot=True)

df.isna().sum()

duplicates = df.duplicated(keep=False)
df['dup_bool'] = duplicates
print(df[df['dup_bool'] == True].count())
df.drop('dup_bool',axis=1,inplace=True)
df.head(1)

df.drop('pickup_datetime',axis=1,inplace=True)

df.head(1)

x = df.drop(['key','fare_amount'],axis=1)
y = df['fare_amount']
x

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.3, random_state=42)

RF_reg = RandomForestRegressor()
RF_reg.fit(xtrain,ytrain)
y_pred = RF_reg.predict(xtest)
MSE = mean_squared_error(ytest, y_pred)
RMSE = np.sqrt(MSE)
r2 = r2_score(ytest, y_pred)
print("Random Forest \nMSE:", MSE)
print("RMSE:", RMSE)
print("R2 score:", r2)

"""Comparing with after scaling

**Using StandardScaler**
"""

from sklearn.preprocessing import StandardScaler
sb = StandardScaler()
x = sb.fit_transform(x)

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.3, random_state=42)

RF_reg = RandomForestRegressor()
RF_reg.fit(xtrain,ytrain)
y_pred = RF_reg.predict(xtest)
MSE = mean_squared_error(ytest, y_pred)
RMSE = np.sqrt(MSE)
r2 = r2_score(ytest, y_pred)
print("Random Forest \nMSE:", MSE)
print("RMSE:", RMSE)
print("R2 score:", r2)

"""**Using MinMaxScaler**"""

from sklearn.preprocessing import MinMaxScaler
m = MinMaxScaler()
x = m.fit_transform(x)

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.3, random_state=42)
RF_reg = RandomForestRegressor()
RF_reg.fit(xtrain,ytrain)
y_pred = RF_reg.predict(xtest)
MSE = mean_squared_error(ytest, y_pred)
RMSE = np.sqrt(MSE)
r2 = r2_score(ytest, y_pred)
print("Random Forest \nMSE:", MSE)
print("RMSE:", RMSE)
print("R2 score:", r2)

"""**StandardScaler improved the R2 score and decreased the RMSE metric**"""